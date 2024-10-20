## What it does.

This tool extracts information from an image of tabular ([JAuswertung](https://github.com/dennisfabri/JAuswertung)) competition results and dumps it into a CSV file.

The accuracy depends on the quality of the image. If the images stem from text-based PDFs or similar, it is highly accurate. If the images stem from image-based PDFs of bad quality, scans, photos of printouts etc., the output should be thoroughly checked.

## How it works.

Install [Telleract](https://github.com/tesseract-ocr/tesseract). Look [here](https://tesseract-ocr.github.io/tessdoc/Installation.html) for instructions and [here](https://github.com/UB-Mannheim/tesseract/wiki) for the Windows installer.

Install the Python requirements.

Run `python main.py path/to/image.jpg`.

There are optional arguments
`--tesseract` to specify the Tesseract executable path (defaults to the default path of the Windows installer) and
`--output` to specify the output CSV file path (defaults to the working directory).

The OCR is done by Tesseract. Information is parsed from hOCR into a table by some heuristics and pattern matching.

## Examples

Input (screenshot of text-based PDF, "Mehrkampfwertung"):
![](examples/1input.png)
Output:
![](examples/1output.png)
Input (screenshot of text-based PDF, "Einzelstreckenwertung"):
![](examples/2input.png)
Output:
![](examples/2output.png)
Input (photo of printout, "Mehrkampfwertung"):
![](examples/3input.jpg)
Output:
![](examples/3output.png)

## Known issues.

Unicode characters in the competitors names are not yet supported. Neither are multiple given names or surnames.