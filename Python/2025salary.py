import pdfplumber
import urllib.request

url = "/https://data-apps.ir.aa.ufl.edu/public/fiscal/2025%20Fall%20Salaries.pdf"
urllib.request.urlretrieve(url, "2025-salaries.pdf")

with pdf_plumber.open("2025-salaries.pdf") as pdf:
    page  = pdf.pages[0]
    table = page.extract_table()
    if table:
        for row in table:
            print(row)