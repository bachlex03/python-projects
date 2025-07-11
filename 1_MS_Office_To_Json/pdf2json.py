import pdf2json
import pypdf
import json



if __name__ == "__main__":
    read_pdf = pypdf.PdfReader('phieu_noi_soi.pdf') # Read the PDF file

    pages = read_pdf.pages
    for page in pages:
        print(page.extract_text())