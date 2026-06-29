🎯 AI Resume Interview Generator

An AI-powered Resume Analysis and Interview Preparation platform built using Python, Streamlit, Google Gemini AI, and SQLite.

The application analyzes resumes, generates ATS scores, provides recruiter feedback, creates company-specific interview questions, and offers an interactive mock interview experience.

⸻

🚀 Features

📄 Resume Analysis

* Upload resumes in PDF format
* Extracts text automatically
* AI-powered resume evaluation

📊 ATS Score Generator

* Calculates ATS compatibility score
* Highlights strengths and weaknesses
* Provides improvement suggestions

🎯 Company-Specific Interview Questions

Supports interview preparation for:

* TCS Digital
* Infosys
* Accenture
* Amazon
* Google
* Microsoft
* General Interviews

💼 Interview Preparation

Generates:

* HR Questions
* Technical Questions
* Project-Based Questions
* DSA Questions

🎤 Mock Interview Mode

* Generate AI interview questions
* Submit answers
* Receive detailed feedback
* Score-based evaluation

📑 Report Generation

* Download Interview Report as TXT
* Download Interview Report as PDF

🗄️ Report History

* Stores previous reports
* ATS score tracking
* Resume history management using SQLite

⸻

🛠️ Tech Stack

Frontend

* Streamlit

Backend

* Python

AI Model

* Google Gemini API

Database

* SQLite

PDF Processing

* PyPDF

PDF Export

* ReportLab

⸻

📂 Project Structure

AI-Resume-Interview-Generator/
│
├── app.py
├── database.py
├── prompts.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── data/

⚙️ Installation

Clone Repository

git clone https://github.com/Vienna3007/AI-Resume-Interview-Generator.git
cd AI-Resume-Interview-Generator

Create Virtual Environment

python -m venv venv

Activate Environment

Windows:

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

⸻

🔑 Environment Variables

Create a .env file:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

Get your Gemini API Key from:

https://aistudio.google.com/app/apikey

⸻

▶️ Run Application

streamlit run app.py

⸻

📸 Application Workflow

1. Upload Resume (PDF)
2. Extract Resume Content
3. Generate ATS Score
4. Receive Recruiter Feedback
5. Generate Interview Questions
6. Practice Mock Interviews
7. Download Report
8. Review History

⸻

🎯 Future Improvements

* Resume Skill Gap Analysis
* Resume Keyword Optimization
* Multiple Resume Comparison
* Voice-Based Mock Interviews
* Interview Performance Analytics
* AI Career Roadmap Generator
* Multi-Language Resume Support

⸻

👩‍💻 Author

Pydi Sri Vaishnavi

B.Tech CSE (Artificial Intelligence)

GitHub: https://github.com/Vienna3007

LinkedIn: https://linkedin.com/in/pydisrivaishnavi

⸻

⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share it with others

⸻

🔗 Live App: https://ai-resume-interview-generator-fefjeqxorjqjkwcgxsxz9d.streamlit.app/

Built with ❤️ using Python, Streamlit and Google Gemini AI.
