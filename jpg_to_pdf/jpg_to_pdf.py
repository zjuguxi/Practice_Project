from PIL import Image
import os
from PyPDF2 import PdfFileMerger
from natsort import natsorted, ns

file_list = []
pdf_list = []

for filename in os.listdir('test'):
    if filename.endswith('jpg'):
        file_list.append(filename)

for filename in file_list:
    im = Image.open('./test/' + filename)
    im.save(filename.strip('.jpg') + '.pdf', resolution = 100)
    pdf_list.append(filename.strip('.jpg') + '.pdf')

pdf_list = natsorted(pdf_list)

print(pdf_list)

outfile = PdfFileMerger()
for file in pdf_list:
    outfile.append(open(file, 'rb'))

outfile.write(open('result.pdf', 'wb'))