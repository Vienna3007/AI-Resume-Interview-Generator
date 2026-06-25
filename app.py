import streamlit as st
import google.generativeai as genai
import os
import re
import pandas as pd

from dotenv import load_dotenv
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from utils import extract_text_from_pdf
from prompts import INTERVIEW_PROMPT, MOCK_INTERVIEW_PROMPT
from database import init_db, save_report, get_reports

# -------------------------
# Setup
# -------------------------

load_dotenv()
init_db()

if "report" not in st.session_state:
    st.session_state.report = ""

if "mock_question" not in st.session_state:
    st.session_state.mock_question = ""

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="AI Resume Interview Generator",
    page_icon="🎯",
    layout="wide"
)

st.markdown("""
<style>
/* Sidebar width */
[data-testid="stSidebar"]{
    min-width:260px;
    max-width:260px;
}
/* Main content spacing */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}
/* Metrics */
[data-testid="metric-container"]{
    background:#1a1d29;
    border-radius:15px;
    padding:20px;
    border:1px solid #30363d;
}
/* Buttons */
.stButton button{
    border-radius:12px;
    height:50px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Helpers
# -------------------------

def extract_ats_score(report):
    match = re.search(r"ATS_SCORE:\s*(\d+)", report)
    if match:
        return int(match.group(1))
    return 0

def create_pdf(text):
    pdf_path = "Interview_Report.pdf"
    doc = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()
    content = []
    for line in text.split("\n"):
        content.append(Paragraph(line, styles["BodyText"]))
    doc.build(content)
    return pdf_path

# -------------------------
# Title
# -------------------------

st.markdown("<h1 style='text-align:center'>🎯 AI Resume Interview Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:18px'>Upload your resume and get ATS analysis, recruiter feedback, interview questions, and mock interview practice.</p>", unsafe_allow_html=True)

# -------------------------
# Sidebar
# -------------------------

with st.sidebar:
    st.title("⚙️ Settings")
    company = st.selectbox(
        "🎯 Target Company",
        ["General", "TCS Digital", "Infosys", "Accenture", "Amazon", "Google", "Microsoft"]
    )
    difficulty = st.select_slider(
        "📈 Question Difficulty",
        options=["Easy", "Medium", "Hard"],
        value="Medium"
    )
    st.markdown("---")
    st.subheader("🚀 Features")
    features = ["ATS Analysis", "HR Questions", "Technical Questions", "Project Questions", "DSA Questions", "Recruiter Feedback", "Mock Interview"]
    for feature in features:
        st.markdown(f"✅ {feature}")
    st.markdown("---")
    st.caption(f"Company: **{company}**\n\nDifficulty: **{difficulty}**")

# -------------------------
# Dashboard
# -------------------------

reports = get_reports()
total_reports = len(reports)
avg_ats = 0

if reports:
    scores = [row[4] for row in reports if row[4] is not None]
    if scores:
        avg_ats = round(sum(scores) / len(scores))

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Reports Generated", total_reports)
with col2:
    st.metric("Average ATS", avg_ats)
with col3:
    st.metric("Companies Supported", 7)

st.divider()

# -------------------------
# Upload Resume
# -------------------------

uploaded_file = st.file_uploader("📄 Upload Resume", type=["pdf"])

if uploaded_file:
    st.success("Resume Uploaded Successfully")
    resume_text = extract_text_from_pdf(uploaded_file)

    with st.expander("📃 View Extracted Resume Text"):
        st.write(resume_text[:5000])

    if st.button("🚀 Generate Interview Report"):
        with st.spinner("Analyzing Resume..."):
            try:
                prompt = INTERVIEW_PROMPT.format(
                    resume=resume_text,
                    company=company,
                    difficulty=difficulty
                )

                response = model.generate_content(prompt)
                report = response.text
                st.session_state.report = report

                ats_score = extract_ats_score(report)
                save_report(uploaded_file.name, company, difficulty, ats_score, report)

                st.success("Report Generated Successfully!")

            except Exception as e:
                st.error(f"Gemini API Error: {e}")
                st.stop()

# -------------------------
# Main Tabs (Outside of Generate Button)
# -------------------------

if st.session_state.report:
    tab1, tab2, tab3 = st.tabs(["📄 Report", "🎤 Mock Interview", "📚 History"])

    with tab1:
        st.subheader("📊 ATS Score")
        report = st.session_state.report
        ats_score = extract_ats_score(report)
        
        st.progress(ats_score / 100)
        st.metric("ATS Score", f"{ats_score}/100")

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="Interview_Report.txt",
            mime="text/plain"
        )

        pdf_file = create_pdf(report)
        with open(pdf_file, "rb") as file:
            st.download_button(
                label="📄 Download PDF Report",
                data=file,
                file_name="Interview_Report.pdf",
                mime="application/pdf"
            )

        clean_report = report.replace(f"ATS_SCORE: {ats_score}", "")
        st.markdown(clean_report)

    with tab2:
        st.subheader("🎤 Mock Interview")
        if st.button("🎲 Generate Question"):
            try:
                question_prompt = f"Generate ONE interview question for a candidate applying to {company} at a {difficulty} level. Return ONLY the question."
                response = model.generate_content(question_prompt)
                st.session_state.mock_question = response.text.strip()
            except Exception as e:
                st.error(f"Gemini Error: {e}")

        if st.session_state.mock_question:
            st.info(st.session_state.mock_question)
            answer = st.text_area("✍️ Your Answer", height=250)

            if st.button("✅ Evaluate Answer"):
                if answer.strip() == "":
                    st.warning("Please enter your answer.")
                else:
                    try:
                        eval_prompt = MOCK_INTERVIEW_PROMPT.format(
                            question=st.session_state.mock_question,
                            answer=answer
                        )
                        eval_response = model.generate_content(eval_prompt)
                        st.markdown(eval_response.text)
                    except Exception as e:
                        st.error(f"Gemini Error: {e}")

    with tab3:
        st.subheader("📚 Previous Reports")
        history = get_reports()
        if history:
            df = pd.DataFrame(history, columns=["ID", "Resume", "Company", "Difficulty", "ATS", "Date"])
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No reports generated yet.")
