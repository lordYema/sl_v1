import streamlit as st
# import PyPDF2

# Function to extract text from PDF
def extract_text_from_pdf(file):
    # pdf_reader = PyPDF2.PdfReader(file)
    # text = ""
    # for page_num in range(len(pdf_reader.pages)):
    #     page = pdf_reader.pages[page_num]
    #     text += page.extract_text()
    return "text"

# Streamlit app
def app():
    st.title("PDF Text Extractor")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        st.success("PDF text extracted successfully!")
        st.write(pdf_text)

        # Print the extracted text in the console
        print(pdf_text)

if __name__ == "__main__":
    app()