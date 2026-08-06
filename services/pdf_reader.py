from pypdf import PdfReader
import re
import string
from bs4 import BeautifulSoup

def extract_text(file):
    text = ""
    with PdfReader(file) as doc:
        for page in doc.pages:
            text += page.extract_text()
    return text