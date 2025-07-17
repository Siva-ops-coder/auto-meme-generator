from flask import Flask, render_template, request, send_from_directory # type: ignore
from meme_generator import generate_meme
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'static/memes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    meme_url = None

    if request.method == 'POST':
        caption = request.form['caption']
        image = request.files.get('image')

        # Use uploaded image or fallback to default
        if image and image.filename != '':
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)
        else:
            image_path = 'default.jpg'  # Put your default image in the root folder

        # Output path
        filename = f"meme_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Generate meme
        generate_meme(image_path, caption, output_path)

        meme_url = f"/static/memes/{filename}"

    return render_template('index.html', meme_url=meme_url)

if __name__ == '__main__':
    app.run(debug=True)
