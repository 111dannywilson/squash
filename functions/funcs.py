import requests

api_key = '563492ad6f91700001000001111ce07f708a4005901e2e883868b6fe'

# endpoint for searching pictures
search_picture_endpoint = "https://pexelsdimasv1.p.rapidapi.com/v1/search"
# endpoint for curated pictures
curated_pictures_endpoint = "https://pexelsdimasv1.p.rapidapi.com/v1/curated"


headers = {
    "Authorization": api_key,
    "X-RapidAPI-Key": "6e6d5c8533msh4e21766a4cc009ap1e6f66jsnae45eb5884c1",
    "X-RapidAPI-Host": "PexelsdimasV1.p.rapidapi.com"
}


# endpoint for searching pictures
def search_picture(query):
    images = []

    querystring = {"query": query, "locale": "en-US",
                   "per_page": "15", "page": "1"}

    try:
        response = requests.get(search_picture_endpoint,
                                headers=headers, params=querystring)
        data = response.json()

        for picture in data["photos"]:
            image = {
                "description": picture['alt'], "image": picture['src']["medium"], "id": picture["id"]}
            images.append(image)

        return {'images': images, 'keyword': query, 'error': ''}
    except:
        return {'images': images, 'keyword': query, 'error': 'Check your internet connection'}


# endpoint for getting pictures on homepage
def curated_photos():

    images = []
    querystring = {"per_page": "15", "page": "1"}

    try:
        response = requests.get(curated_pictures_endpoint,
                                headers=headers, params=querystring)
        data = response.json()

        for picture in data["photos"]:
            image = {
                "description": picture['alt'], "image": picture['src']["medium"], "id": picture["id"]}
            images.append(image)
        return {'images': images, 'error': ''}
        # return 'hi'

    except:
        # return 'hey'
        return {'images': images, 'error': 'Check your internet connection'}


# displaying clicked picture
def get_clicked_picture(picture_id):
    url = f"https://pexelsdimasv1.p.rapidapi.com/v1/photos/{picture_id}"
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

# get_clicked_picture(picture_id)
