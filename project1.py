from    PyPDF2  import PdfMerger
Allpdf=["1.pdf","2.pdf"]
Ourmarger=PdfMerger()
for newpdf in Allpdf:
    Ourmarger.append(newpdf)

Ourmarger.write("habib.pdf")