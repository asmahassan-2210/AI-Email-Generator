✉️ AI Email Generator

An AI-powered email generation web application built with FastAPI and Google Gemini. The application allows users to enter a recipient name, email purpose, and preferred tone, then automatically generates a complete, polished email using AI.

🌟 Features
✉️ AI Email Generation — Generate complete emails using Google Gemini.
👤 Recipient Input — Specify the person receiving the email.
📝 Email Purpose — Describe what the email should be about.
🎨 Multiple Tones — Choose from:
Professional
Friendly
Formal
📋 Copy Email — Copy the generated email with one click.
⚡ FastAPI Backend — Lightweight and efficient API backend.
🌐 Interactive Web Interface — Clean and responsive frontend.
🔐 Environment Variables — API key is securely stored in .env.
📱 Responsive Design — Works across desktop and mobile screen sizes.
🛠️ Technologies Used
Technology	Purpose
Python	Backend programming
FastAPI	Web framework and API
Google Gemini	AI email generation
HTML5	Frontend structure
CSS3	Styling and responsive design
JavaScript	Frontend interaction and API communication
Uvicorn	ASGI server
python-dotenv	Environment variable management
📂 Project Structure
AI Email Generator/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
File Description

main.py
Contains the FastAPI application, Gemini API integration, API endpoints, and static file configuration.

templates/index.html
Contains the main user interface.

static/style.css
Contains the styling, layout, colors, buttons, forms, cards, and responsive design.

static/script.js
Handles form submission, communication with the FastAPI /generate endpoint, loading state, displaying the generated email, and the copy button.

.env
Stores the Gemini API key securely.

requirements.txt
Contains the Python dependencies required to run the project.

🔄 How It Works

The application follows this workflow:

User
  │
  ▼
Enter Recipient Name
  │
  ▼
Enter Email Purpose
  │
  ▼
Select Email Tone
  │
  ▼
Click "Generate Email"
  │
  ▼
JavaScript sends request
to FastAPI /generate
  │
  ▼
FastAPI sends prompt
to Google Gemini
  │
  ▼
Gemini generates email
  │
  ▼
FastAPI returns response
  │
  ▼
JavaScript displays email
  │
  ▼
User can copy the email
🚀 Installation
1. Clone the Repository
git clone https://github.com/your-username/AI-Email-Generator.git

Navigate into the project:

cd AI-Email-Generator
2. Create a Virtual Environment

Windows:

python -m venv venv

Activate it:

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt

Or:

pip install fastapi uvicorn google-genai python-dotenv
🔑 Configure Gemini API

Create a .env file in the project root:

GEMINI_API_KEY=your_gemini_api_key_here

Replace:

your_gemini_api_key_here

with your actual Google Gemini API key.

Important: Never upload your .env file or API key to GitHub.

📋 Requirements

Your requirements.txt should contain:

fastapi
uvicorn
google-genai
python-dotenv
▶️ Run the Application

Start the FastAPI server:

python -m uvicorn main:app --reload

You should see something similar to:

Uvicorn running on http://127.0.0.1:8000

Open your browser and visit:

http://127.0.0.1:8000
🖥️ Using the Application
Enter the Recipient Name.
Enter the Email Purpose.
Select the desired Email Tone.
Click Generate Email.
The application sends the information to the FastAPI backend.
Google Gemini generates the email.
The generated email appears on the right side.
Click Copy to copy the email.
🔌 API Endpoint
Generate Email

Endpoint:

POST /generate
Request Body
{
    "recipient": "Ahmed Khan",
    "purpose": "Requesting leave from work",
    "tone": "Professional"
}
Response
{
    "success": true,
    "email": "Subject: Leave Request\n\nDear Mr. Khan,\n\n..."
}
🎨 User Interface

The interface contains two main sections:

Create Your Email

Users provide:

Recipient name
Email purpose
Preferred tone
Generated Email

The AI-generated email is displayed here with a Copy button for convenience.

🔐 Security

The Gemini API key is loaded through an environment variable:

load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")

Make sure .gitignore contains:

.env
venv/
__pycache__/
*.pyc

This prevents sensitive credentials and unnecessary Python files from being committed to GitHub.

🧪 Example
Input

Recipient Name:

Mr. Ahmed Khan

Email Purpose:

Requesting leave for two days due to a family commitment.

Tone:

Professional
Output

The application generates a complete email containing:

Subject
Greeting
Main message
Closing
Professional wording
📌 Future Improvements

Possible improvements include:

📧 Direct email sending
👥 More recipient types
🎭 Additional tone options
🌍 Multiple language support
💾 Email history
📄 Export email as PDF
🔐 User authentication
☁️ Cloud deployment
📊 Email generation history and analytics
🎓 Project Objective

The objective of this project is to demonstrate how Generative AI can be integrated with a FastAPI web application to automate email writing. It combines a Python backend, an interactive frontend, and Google's Gemini AI model to create personalized emails based on user-provided information.

👩‍💻 Author

Asma Hassan

Developed as an AI/Generative AI project using FastAPI, Python, JavaScript, and Google Gemini.

⭐ Acknowledgment

This project was developed as part of practical learning in Generative AI, API integration, FastAPI, and prompt engineering.
