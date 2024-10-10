from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()

# add all page to writer
for page_num in range(len(reader.pages)):
    writer.add_page(reader.pages[page_num])

# update PDF element (e.g. title)
writer.add_metadata({
    '/Title': '113-CSIE-S003'
})

with open("output.pdf", "wb") as output_pdf:
    writer.write(output_pdf)
