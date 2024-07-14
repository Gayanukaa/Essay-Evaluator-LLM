import streamlit as st
import dspy
from fpdf import FPDF
import base64

# Configure the model
ollama_model = dspy.OllamaLocal(
    model="llama2",
    model_type='text',
    max_tokens=500,
    temperature=0.0,
    top_p=0.8,
    frequency_penalty=1.17,
    top_k=40
)
dspy.settings.configure(lm=ollama_model)

# Initialize the sentiment model
sentiment_model = dspy.Predict('sentence -> sentiment')

def generate_remarks(essay_text, criteria):
    criteria_str = ", ".join(criteria)
    prompt = f"Evaluate this essay based on the following criteria: {criteria_str}. Provide remarks: {essay_text} all in one paragraph"
    response = ollama_model(prompt)
    if isinstance(response, list) and response:
        remarks = "\n".join(response)
        return remarks.strip()
    raise ValueError("Unexpected response format from Ollama model")

def analyze_sentiment(remarks):
    sentiment = sentiment_model(sentence=remarks)
    sentiment = sentiment['sentiment'].strip().lower()
    return sentiment

def grade_essay(sentiment):
    if "excellent" in sentiment:
        return "A"
    elif "good" in sentiment:
        return "B"
    elif "neutral" in sentiment:
        return "C"
    elif "bad" in sentiment:
        return "S"
    elif "very poor" in sentiment:
        return "D"
    elif "fail" in sentiment:
        return "F"

def create_pdf(remarks, grade):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, "Evaluation Remarks:")
    pdf.multi_cell(0, 10, remarks)

    pdf.ln(10)
    pdf.set_font("Arial", size=14)
    pdf.cell(0, 10, f"Grade: {grade}", 0, 1, 'C')

    return pdf

def convert_pdf_to_base64(pdf):
    pdf_output = pdf.output(dest='S').encode('latin1')
    b64 = base64.b64encode(pdf_output).decode('utf-8')
    href = f'<a href="data:application/pdf;base64,{b64}" download="evaluation.pdf">Download PDF</a>'
    return href

def main():
    st.title("Essay Evaluation Tool")

    st.write("Paste your essay text below for evaluation:")
    essay_text = st.text_area("Essay Text")

    criteria = ["clarity", "coherency", "grammar"]

    if st.button("Evaluate Essay"):
        if essay_text:
            with st.spinner("Evaluating your essay..."):
                try:
                    remarks = generate_remarks(essay_text, criteria)
                    sentiment = analyze_sentiment(remarks)
                    grade = grade_essay(sentiment)

                    st.subheader("Evaluation Remarks")
                    st.write(remarks)

                    st.subheader("Grade")
                    st.markdown(f"<h1 style='color: green;'>{grade}</h1>", unsafe_allow_html=True)

                    pdf = create_pdf(remarks, grade)
                    pdf_link = convert_pdf_to_base64(pdf)
                    st.markdown(pdf_link, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please paste the essay text to be evaluated.")

if __name__ == "__main__":
    main()
