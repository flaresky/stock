# -*- coding: utf-8 -*-

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator

# Open a PDF file.
fp = open('/Users/flaresky/Downloads/2015.PDF', 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
document = PDFDocument(parser)
# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# # Create a PDF device object.
# device = PDFDevice(rsrcmgr)
# # Create a PDF interpreter object.
# interpreter = PDFPageInterpreter(rsrcmgr, device)

# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

layout = None
# Process each page contained in the document.
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for x in layout:
#         print x
        if isinstance(x, LTTextBoxHorizontal):
            print x.get_text().encode('utf-8')
        else:
            print x
    break
#     print type(layout)
#     print layout
#     print dir(layout)
#     break
# print dir(layout)