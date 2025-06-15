from readPDF import read_pdf_text
import config  
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

def llm_response():
    return read_pdf_text(config.PDFfilePath)

def llm():
    content = llm_response()
    api_key = os.getenv("GOOGLE_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[f'''
Create flashcard front and back, made from this {content}. 
Create a 2D list of questions and answers with correct answers. 
Make sure that the questions match this format:
reply with array only nothing else
[["Question?","correct answer"],["Question", "correct answer",] and more questions...]
make a new response every time
''']
    )

    with open("data.txt", 'w', encoding='utf-8') as f:
        f.write(response.text)
