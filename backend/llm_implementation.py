from readPDF import read_pdf_text
import config  
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

def pdf_response():
    return read_pdf_text(config.PDFfilePath)
def text_response():
    return config.rawTextData

def llm():
    content = config.rawTextData.strip() if config.rawTextData else ""
    if not content and config.PDFfilePath:
        content = read_pdf_text(config.PDFfilePath).strip()
    if not content:
        print("No content to process")
        return

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise Exception("GOOGLE_API_KEY not found in environmentvariables")

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[f'''
Create flashcard front and back, made from this {content}. 
Create a 2D list of questions and answers with correct answers. 
Make sure that the questions match this format:
reply with array only nothing else
[["Question?","correct answer"],["Question", "correct answer",] and more upto 10 questions...]
make a new response every time
''']
        )
        with open("data.txt", 'w', encoding='utf-8') as f:
            f.write(response.text)

    except Exception as e:
        print("LLM processin failed:", str(e))
        raise

