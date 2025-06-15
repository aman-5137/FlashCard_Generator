# Flashcard Generator using PDF + Gemini LLM + Flask

This project allows you to upload a PDF file (such as a textbook or study material), automatically extract its content, generate flashcards using Google's Gemini API, and present them in an interactive web interface.

---
##  Features

-  Upload a PDF file
-  Automatically extracts text from PDF
-  Uses Gemini (Google's LLM) to generate questions and answers
-  Displays them as interactive flashcards
-  Navigate one flashcard at a time
-  Reveal answers on click
-  Shows "Loading..." while generating flashcards

---

## Tech Stack

- **Backend**: Python, Flask, Google Gemini API
- **Frontend**: HTML, CSS, JavaScript
- **PDF Processing**: PyPDF2 (via `readPDF.py`)
- **Environment Config**: Python `dotenv`
- **LLM Output Parsing**: Custom Python logic to convert Gemini response into a 2D array

---

## Folder Structure

flashcard_generator/
├── backend/
│ ├── main.py # Flask app entry point
│ ├── llm_implementation.py # Handles Gemini LLM call
│ ├── convert_into_2dArr.py # Parses Gemini response to 2D list
│ ├── readPDF.py # Extracts text from uploaded PDF
│ ├── config.py # Shared global variable for PDF file path
│ ├── uploads/ # Stores uploaded PDFs
│ ├── data.txt # Stores Gemini output
│ └── .env # Contains your Google API Key
├── templates/
│ └── index.html # Interactive flashcard UI
└── README.md 

## Install dependencies
pip install -r requirements.txt

pip install flask flask-cors python-dotenv google-generativeai PyMuPDF

## Create .env file
GOOGLE_API_KEY=your_google_api_key_here
You must enable Gemini API access and get your key from Google AI Studio


## Author
Aman Kumar Yadav

Thanks for visting and feel free to raise issues :)
