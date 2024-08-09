import subprocess


class OcrTool:

    def __init__(self, tesseract_executable_path):
        self.tesseract_executable_path = tesseract_executable_path

    def get_hocr(self, image_path):
        hocr_output = subprocess.getoutput(f'"{self.tesseract_executable_path}" {image_path} - --psm 4 hocr')
        return hocr_output
