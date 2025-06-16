from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from convert_into_2dArr import extract_2d_array_from_string
from llm_implementation import llm, text_response
import os
import config  

quiz_data = []

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/flashcards')
def get_flashcards():
    return jsonify(quiz_data)


@app.route('/upload_text', methods=['POST'])
def upload_text():
    global quiz_data
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    raw_text = data['text']
    config.rawTextData = raw_text  

    llm()
    quiz_data = extract_2d_array_from_string()
    return jsonify(quiz_data)
    


@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    global quiz_data

    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and file.filename.endswith('.pdf'):
        filepath = os.path.join('uploads', file.filename)
        os.makedirs('uploads', exist_ok=True)
        file.save(filepath)

        config.PDFfilePath = filepath  

        llm()  

        quiz_data = extract_2d_array_from_string()

        return jsonify(quiz_data)

    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True)
