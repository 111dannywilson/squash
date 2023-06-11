from flask import Blueprint, render_template, request, redirect
from functions.funcs import search_picture, curated_photos
import os

# variables

views = Blueprint('views', __name__)

img = os.path.join('static', 'Images')
a_text = ''


def get_picture(filename): return os.path.join(img, filename)


# pictures = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg',
# '6.jpg', '7.png', '8.jpg', '9.jpg', '10.jpg']

# pictures = [
#     {"image": get_picture('1.jpg'), "height": "370px", "width": "400px"},
#     {"image": get_picture('2.jpg'), "height": "329px", "width": "200px"},
#     {"image": get_picture('3.jpg'), "height": "340px", "width": "330px"},
#     {"image": get_picture('4.jpg'), "height": "380px", "width": "600px"},
#     {"image": get_picture('5.jpg'), "height": "449px", "width": "300px"},
#     {"image": get_picture('6.jpg'), "height": "330px", "width": "430px"},
# ]


pictures = [
    {"image": get_picture('1.jpg')},
    {"image": get_picture('2.jpg')},
    {"image": get_picture('3.jpg')},
    {"image": get_picture('4.jpg')},
    {"image": get_picture('5.jpg')},
    {"image": get_picture('6.jpg')},
]

# routes
# home route(curated pictures)


@views.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        query = request.form.get('query')

        return redirect(f'search/{query}')

    results = []
    curated = curated_photos()

    for data in curated['images']:
        image = {"description": data["description"], "image": data["image"]}
        results.append(image)

    trending = ['travel,', 'mountain,', 'technology,', 'food,', 'business']
    get_started = ['Cats', 'Sky', 'Space', 'Family', 'Ferrari', 'Moon']

    return render_template('home.html', results=results, potential_search=get_started, trending=trending, pictures=pictures)


# search-results route
@views.route('/search/<keyword>', methods=['GET', 'POST'])
def search(keyword):
    results = None
    # query = None
    # picture_id = None

    if request.method == 'POST':
        search_query = request.form.get('query')
        results = search_picture(search_query)
        # for data in results["images"]:
        #     print(data['id'])
        if results['images'] == []:
            # print('empty')
            results['error'] = 'Please input a valid keyword'
            # print(results['keyword'])

        return render_template('search.html', pictures=results["images"], keyword=keyword, error=results["error"])

    results = search_picture(keyword)
    return render_template('search.html', pictures=results["images"], keyword=keyword, error=results["error"])


@views.route('/download')
def download_picture():
    return render_template('download.html')


#  <!-- style="height: {{data['height']}}; -->
