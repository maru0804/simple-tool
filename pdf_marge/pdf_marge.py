import PyPDF2
import glob
import time
from natsort import natsorted

start = time.time()

pdflist =glob.glob("pdf/*.pdf")

merger = PyPDF2.PdfFileMerger()

for i in natsorted(pdflist):
    merger.append(i)

merger.write('pdf_merge.pdf')
merger.close()

endtime = time.time() - start

print(endtime)