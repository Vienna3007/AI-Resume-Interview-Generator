from pypdf import PdfReader

def extract_text_from_pdf(uploaded_file):

    text = ""

    try:

        pdf = PdfReader(uploaded_file)

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    except Exception as e:

        return f"Error reading PDF: {e}"

    return text