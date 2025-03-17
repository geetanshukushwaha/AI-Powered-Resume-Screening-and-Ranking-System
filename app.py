import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract text from a PDF file
def get_pdf_text(pdf_file):
    reader = PdfReader(pdf_file)
    return "".join([page.extract_text() for page in reader.pages if page.extract_text()])

# Compute similarity scores
def compute_similarity(job_desc, resume_texts):
    documents = [job_desc] + resume_texts
    tfidf_matrix = TfidfVectorizer().fit_transform(documents).toarray()
    similarity_scores = cosine_similarity([tfidf_matrix[0]], tfidf_matrix[1:]).flatten()
    return similarity_scores

# Streamlit UI setup
st.title("AI-Powered Resume Ranking System")

st.header("Job Description")
job_description = st.text_area("Paste the job description here")

st.header("Upload Resumes (PDF Format)")
resume_files = st.file_uploader("Upload multiple resumes", type=["pdf"], accept_multiple_files=True)

if resume_files and job_description:
    resume_texts = [get_pdf_text(file) for file in resume_files]
    scores = compute_similarity(job_description, resume_texts)
    
    # Display ranked resumes
    ranking_df = pd.DataFrame({"Resume File": [file.name for file in resume_files], "Match Score": scores})
    ranking_df = ranking_df.sort_values(by="Match Score", ascending=False)
    
    st.subheader("Ranking Results")
    st.dataframe(ranking_df)
