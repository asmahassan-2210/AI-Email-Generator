import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from google import genai


# =========================================================
# PATH SETUP
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")


# =========================================================
# FASTAPI APP
# =========================================================

app = FastAPI(
    title="AI Email Generator",
    description="Generate professional emails using Google Gemini",
    version="1.0"
)


# =========================================================
# SERVE STATIC FILES
# =========================================================
# This connects:
#
# /static/style.css  -> static/style.css
# /static/script.js  -> static/script.js
#
# Without this, your CSS and JavaScript will not load.

app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static"
)


# =========================================================
# GEMINI CLIENT
# =========================================================

client = None

if API_KEY:
    client = genai.Client(api_key=API_KEY)


# =========================================================
# REQUEST MODEL
# =========================================================

class EmailRequest(BaseModel):
    recipient: str
    purpose: str
    tone: str


# =========================================================
# HOME PAGE
# =========================================================

@app.get("/")
async def home():
    """
    Open the index.html file from the templates folder.
    """

    return FileResponse(
        TEMPLATES_DIR / "index.html"
    )


# =========================================================
# GENERATE EMAIL
# =========================================================

@app.post("/generate")
async def generate_email(data: EmailRequest):

    # Check API key
    if not API_KEY:

        return {
            "success": False,
            "message": (
                "Gemini API key is missing. "
                "Please check your .env file."
            )
        }


    # Check Gemini client
    if client is None:

        return {
            "success": False,
            "message": "Gemini client could not be initialized."
        }


    # =====================================================
    # PROMPT
    # =====================================================

    prompt = f"""
You are an AI Email Generator.

Write a complete and polished email based on the information below.

Recipient Name:
{data.recipient}

Email Purpose:
{data.purpose}

Tone:
{data.tone}

Requirements:

1. Create a suitable subject line.
2. Include an appropriate greeting.
3. Write a complete and meaningful email.
4. Make the email clear, natural, and grammatically correct.
5. Follow the requested tone.
6. Include a suitable closing.
7. Return ONLY the generated email.
8. Do not explain what you did.
"""


    # =====================================================
    # CALL GEMINI
    # =====================================================

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )


        # Get generated text
        generated_email = response.text


        # Check empty response
        if not generated_email:

            return {
                "success": False,
                "message": "Gemini returned an empty response."
            }


        # =================================================
        # RETURN SUCCESS
        # =================================================

        return {
            "success": True,
            "email": generated_email
        }


    # =====================================================
    # ERROR HANDLING
    # =====================================================

    except Exception as error:

        print("\n==============================")
        print("GEMINI ERROR")
        print("==============================")
        print(error)
        print("==============================\n")


        return {
            "success": False,
            "message": str(error)
        }


# =========================================================
# RUN SERVER
# =========================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )