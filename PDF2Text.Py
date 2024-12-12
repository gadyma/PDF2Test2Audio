import PyPDF2
import re

def pdf_to_text(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Extract text from all pages
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    return text

def remove_newlines(text):
    # Use regex to replace newlines not preceded by a period
    return re.sub(r'(?<![.?!,])(\n|\r|\r\n)', ' ', text)

def save_to_file(text, file_path):
    # Open the file in write mode and save the text
    with open(file_path, 'w') as file:
        file.write(text)

# Example usage
pdf_path = 'AIreport.pdf'
file_path = 'AIreport.txt'
text = pdf_to_text(pdf_path)
processed_text = remove_newlines(text)

print(processed_text)
save_to_file(processed_text, file_path)