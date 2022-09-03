from PyPDF2 import PdfMerger
import sys

files = sys.argv[1:]
merger = PdfMerger()

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()