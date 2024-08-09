## What it does.

This tool extracts information from an image of tabular competition results and dumps it into a CSV file.

The accuracy depends on the quality of the image. If the images stem from text-based PDFs or similar, it is highly accurate. If the images stem from image-based PDFs of bad quality, scans, photos etc., it is less accurate. In my experience, this manifests mostly in missing information, and not so much in incorrect information.

## How it works.

Install [Telleract](https://github.com/tesseract-ocr/tesseract). Look [here](https://tesseract-ocr.github.io/tessdoc/Installation.html) for instructions and [here](https://github.com/UB-Mannheim/tesseract/wiki) for the Windows installer.

Install the Python requirements.

Run `python main.py path/to/image.jpg`.

There are optional arguments
`--tesseract` to specify the Tesseract executable path (defaults to the default path of the Windows installer) and
`--output` to specify the output CSV file path (defaults to the working directory).

The OCR is done by Tesseract. Information is parsed from hOCR into a table by some heuristics and pattern matching.

## Known issues.

Unicode characters in the competitors names are not yet supported. Neither are multiple given names or surnames.