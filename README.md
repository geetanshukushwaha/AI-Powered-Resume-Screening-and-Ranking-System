# AI-Powered-Resume-Screening-and-Ranking-System

#### **Overview**  
This project automates resume screening using **Natural Language Processing (NLP)**. It extracts text from **PDF resumes**, processes a **job description**, and ranks candidates based on **TF-IDF vectorization** and **cosine similarity**.  

#### **Technologies Used**  
- **Python 3.x**  
- **Streamlit** (for UI)  
- **PyPDF2** (for PDF text extraction)  
- **Scikit-learn** (for TF-IDF & similarity calculation)  
- **Pandas** (for data handling)  

#### **Installation & Usage**  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/resume-screening.git  
   cd resume-screening  
   ```  

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt  
   ```  

3. **Run the Application**  
   ```bash
   streamlit run app.py  
   ```  

#### **How It Works**  
- Enter the **job description**.  
- Upload multiple **PDF resumes**.  
- The system extracts text and ranks resumes **based on similarity** to the job description.  

#### **Future Enhancements**  
- Add **OCR support** for scanned resumes.  
- Improve ranking using **deep learning models (BERT/GPT)**.  
- Integrate with **ATS (Applicant Tracking Systems)**.  

