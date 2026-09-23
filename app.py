from flask import Flask, render_template, request
import os

from ocr import extract_text
from translator import translate_text

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/extract', methods=['POST'])
def extract():

    file = request.files['image']

    if file.filename == '':
        return "No file selected"

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    text = extract_text(filepath)

    return render_template(
        'index.html',
        extracted_text=text
    )


@app.route('/translate', methods=['POST'])
def translate():

    text = request.form['text']
    language = request.form['language']

    translated = translate_text(text, language)

    return render_template(
        'index.html',
        extracted_text=text,
        translated_text=translated
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)