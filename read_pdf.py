from langchain_core.tools import tool
import io
import PyPDF2
import requests

url = "https://arxiv.org/pdf/2509.05276v1"
# step 1: Access Pdf via URL
response = requests.get(url)
# print(response.content)

# # step 2: convert to bytes
pdf_file = io.BytesIO(response.content)
# print(pdf_file)

# step 3: Retrieve text from PDF
pdf_reader = PyPDF2.PdfReader(pdf_file)
print(len(pdf_reader.pages))
