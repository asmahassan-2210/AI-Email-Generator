import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from google import genai


# --------------------------------------------------
# Project setup
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")


# --------------------------------------------------
# FastAPI
# --------------------------------------------------

app = FastAPI(
    title="AI Email Generator"
)


# --------------------------------------------------
# Gemini
# --------------------------------------------------

client = None

if API_KEY:
    client = genai.Client(
        api_key=API_KEY
    )


# --------------------------------------------------
# Request model
# --------------------------------------------------

class EmailRequest(BaseModel):

    recipient: str
    purpose: str
    tone: str


# --------------------------------------------------
# Home page
# --------------------------------------------------

@app.get("/")
async def home():

    return FileResponse(
        BASE_DIR / "static" / "index.html"
    )


# --------------------------------------------------
# Generate Email
# --------------------------------------------------

@app.post("/generate")
async def generate_email(data: EmailRequest):

    # Check API key

    if not API_KEY:

        return {
            "success": False,
            "message": "Gemini API key is missing. Check your .env file."
        }


    # Prompt

    prompt = f"""
You are a professional email writing assistant.

Generate a complete email using the following information.

Recipient Name:
{data.recipient}

Email Purpose:
{data.purpose}

Tone:
{data.tone}

Requirements:

- Include a suitable subject line.
- Include an appropriate greeting.
- Write a complete email.
- Make it clear and natural.
- Follow the requested tone.
- Include a suitable closing.
- Return only the email.
"""


    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        generated_email = response.text


        if not generated_email:

            return {
                "success": False,
                "message": "Gemini returned an empty response."
            }


        return {
            "success": True,
            "email": generated_email
        }


    except Exception as error:

        print("\nGemini Error:")
        print(error)

        return {
            "success": False,
            "message": str(error)
        }