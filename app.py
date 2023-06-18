from website import create_app
from flask import Flask, render_template, url_for

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
