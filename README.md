# 🎯 AI Resume Interview Generator

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge\&logo=streamlit)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-4285F4?style=for-the-badge\&logo=google)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge\&logo=sqlite)

</p>

<p align="center">
An AI-powered Resume Analysis & Interview Preparation Platform built with <b>Python</b>, <b>Streamlit</b>, <b>Google Gemini AI</b>, and <b>SQLite</b>.
</p>

<p align="center">

🔗 **Live Demo:** https://ai-resume-interview-generator-fefjeqxorjqjkwcgxsxz9d.streamlit.app/

</p>

---

# 📖 Overview

AI Resume Interview Generator helps students and job seekers prepare for technical interviews by analyzing resumes using Google's Gemini AI.

The application generates:

* 📊 ATS Score
* 💼 Recruiter Feedback
* 🎯 Company-specific Interview Questions
* 🧠 Technical & DSA Questions
* 🎤 AI Mock Interview Evaluation
* 📄 Downloadable Interview Reports

---

# ✨ Features

## 📄 Resume Analysis

* Upload Resume in PDF format
* Automatic text extraction
* AI-powered resume evaluation

## 📊 ATS Score Analysis

* ATS Compatibility Score
* Resume Strengths
* Weaknesses
* Resume Improvement Suggestions

## 💼 Company-Specific Interview Questions

Choose from:

* General
* TCS Digital
* Infosys
* Accenture
* Amazon
* Google
* Microsoft

## 🎯 AI Interview Generator

Automatically generates:

* HR Interview Questions
* Technical Questions
* Project-Based Questions
* DSA Questions

## 🎤 AI Mock Interview

* Generate interview questions
* Submit answers
* AI evaluates your response
* Strengths & Weaknesses
* Improved Answer
* Score out of 10

## 📑 Report Generation

* TXT Report
* PDF Report

## 🗄️ Report History

* Stores previous reports
* ATS Score History
* SQLite Database Integration

---

# 🛠️ Tech Stack

| Category       | Technology       |
| -------------- | ---------------- |
| Language       | Python           |
| Frontend       | Streamlit        |
| AI Model       | Google Gemini AI |
| Database       | SQLite           |
| PDF Processing | PyPDF            |
| PDF Export     | ReportLab        |

---

# 📂 Project Structure

```text
AI-Resume-Interview-Generator/
│
├── app.py                  # Main Streamlit application
├── database.py             # SQLite database operations
├── prompts.py              # AI prompt templates
├── utils.py                # PDF text extraction utilities
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
├── .streamlit/
│   └── config.toml
│
└── data/
    └── database.db
```

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Vienna3007/AI-Resume-Interview-Generator.git

cd AI-Resume-Interview-Generator
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment (Windows):

```bash
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Generate your API key from:

https://aistudio.google.com/app/apikey

---

## 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

# 📸 Application Workflow

```text
Upload Resume
      │
      ▼
Extract PDF Text
      │
      ▼
Gemini AI Analysis
      │
      ▼
ATS Score Generation
      │
      ▼
Interview Questions
      │
      ▼
Mock Interview
      │
      ▼
Download Report
```

---

# 🔮 Future Enhancements

* 🎙️ Voice-Based Mock Interviews
* 📈 Resume Skill Gap Analysis
* 📊 Interview Performance Dashboard
* 🌐 Multi-Language Resume Support
* 🤖 AI Career Roadmap Generator
* 📑 Resume Comparison
* ☁️ Cloud Database Integration

---

# 👩‍💻 Author

**Pydi Sri Vaishnavi**

B.Tech – Computer Science & Engineering (Artificial Intelligence)

🔗 GitHub: https://github.com/Vienna3007

🔗 LinkedIn: https://linkedin.com/in/pydisrivaishnavi

---

# ⭐ Show Your Support

If you found this project helpful:

⭐ Star this repository

🍴 Fork this repository

💡 Share your feedback and suggestions

---

<p align="center">

Made with ❤️ using **Python**, **Streamlit**, and **Google Gemini AI**

</p>
