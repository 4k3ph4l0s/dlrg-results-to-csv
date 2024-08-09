from OcrTool import OcrTool
from HocrParser import HocrParser
from Tabulator import Tabulator
import csv


# Put the path to your tesseract executable here
tesseract_executable_path = "C:/Program Files/Tesseract-OCR/tesseract.exe"
# Path to your image
image_path = "photo1.jpg"

# Perform OCR
hocr = OcrTool(tesseract_executable_path).get_hocr(image_path)
# Parse hOCR into a more useful structure
parsed_data = HocrParser().parse_hocr(hocr)
# Build the table
table = Tabulator().get_as_table(parsed_data)
# Replace commas
table = [[cell.replace(',', '.') for cell in row] for row in table]
# Write CSV
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(table)
