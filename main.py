import argparse
import csv
import cv2
import os
from OcrTool import OcrTool
from HocrParser import HocrParser
from Tabulator import Tabulator


def main(image_path, tesseract_executable_path, output_csv_path):
    # Scale image (3000px width seems to give sufficient OCR accuracy)
    image = cv2.imread(image_path)
    scale_factor = 3000 / image.shape[1]
    image = cv2.resize(image, (0, 0), fx=scale_factor, fy=scale_factor)
    cv2.imwrite("scaled_image.jpg", image)
    image_path = "scaled_image.jpg"
    # Perform OCR
    hocr = OcrTool(tesseract_executable_path).get_hocr(image_path)
    # Parse hOCR into a more useful structure
    parsed_data = HocrParser().parse_hocr(hocr)
    # Build the table
    table = Tabulator().get_as_table(parsed_data)
    # Replace commas
    table = [[cell.replace(',', '.') for cell in row] for row in table]
    # Write CSV
    with open(output_csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(table)
    # Delete the scaled image
    os.remove(image_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", help="Path to the image file to process")
    parser.add_argument("--tesseract", default="C:/Program Files/Tesseract-OCR/tesseract.exe", help="Path to the Tesseract executable")
    parser.add_argument("--output", default="output.csv", help="Path to the output CSV file")

    args = parser.parse_args()
    main(args.image_path, args.tesseract, args.output)
