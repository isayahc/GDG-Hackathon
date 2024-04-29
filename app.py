from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    # URL of the image you want to display
    image_url = "https://images.pexels.com/videos/852286/free-video-852286.jpg"

    # Download the image
    image_response = requests.get(image_url)
    image_data = image_response.content

    # Save the image to a temporary file
    with open('static/temp_image.jpg', 'wb') as f:
        f.write(image_data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
