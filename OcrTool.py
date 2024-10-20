import subprocess


class OcrTool:

    def __init__(self, tesseract_executable_path):
        self.tesseract_executable_path = tesseract_executable_path

    def get_hocr(self, image_path):
        # --psm 6 should be slightly superior to --psm 4 here because the text size does not vary much (more testing needed)
        hocr_output = subprocess.getoutput(f'"{self.tesseract_executable_path}" {image_path} - --psm 6 hocr')
        return hocr_output
