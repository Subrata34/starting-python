import PyPDF2
files=open("1.pdf","rb")
reader=PyPDF2.PdfFileReader(files)
print(reader.numPages)