from PyPDF2 import PdfFileReader,PdfFileWriter
import requests
target_file = 'Crypto Ass1.pdf'
output_file = open('output_rotated.pdf','wb')

pdf = PdfFileReader(target_file)
writer = PdfFileWriter()

num_page = pdf.getNumPages()
angle = 90
rotated_page = 1

for i in range(num_page):
    page = pdf.getPage(i)
    if rotated_page == i:
        page.rotateClockwise(angle)
    writer.addPage(page)

writer.write(output_file)

output_file.close()