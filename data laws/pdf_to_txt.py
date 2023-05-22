import os 
from tqdm.auto import tqdm
from PyPDF2 import PdfReader 
for filename in tqdm(os.listdir("data/pdf_2"), 'File', position=0):
    with open(os.path.join("data/pdf", filename), 'rb') as pdfFileObj:
        reader = PdfReader(pdfFileObj)
        pages = reader.pages
        txtFileObj = open(r"data/txt_2/"+filename[:-4]+'.txt',"a", encoding="utf-8")
        for page in tqdm(pages, 'Page', position=1, leave=False):
            text = page.extract_text()
            txtFileObj.write(text)    
        txtFileObj.close()