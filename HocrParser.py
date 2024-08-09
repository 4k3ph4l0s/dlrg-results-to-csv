import re
from bs4 import BeautifulSoup


class HocrParser:

    def __init__(self, number_of_events = 0):
        self.number_of_events = number_of_events
        self.parsed_data = []
    
    def parse_hocr(self, hocr):
        soup = BeautifulSoup(hocr, "html.parser")

        for line in soup.find_all('span', class_='ocr_line'):
            line_bbox = self.get_bbox(line['title'])
            line_data = {'bbox': line_bbox, 'words': []}
            
            words = line.find_all('span', class_='ocrx_word')
            surname = None
            firstname = None
            
            for i, word in enumerate(words):
                word_text = word.text.strip()
                word_bbox = self.get_bbox(word['title'])
                
                if not surname:
                    # TODO unicode characters and weird names
                    if re.match(r'\w+,$', word_text):
                        surname = word_text[:-1]  # Remove trailing comma
                        if i + 1 < len(words):
                            firstname = words[i+1].text.strip()
                        
                        line_data['words'].append({
                            'type': 'surname',
                            'text': surname,
                            'bbox': word_bbox
                        })
                        if firstname:
                            line_data['words'].append({
                                'type': 'firstname',
                                'text': firstname,
                                'bbox': self.get_bbox(words[i+1]['title'])
                            })
                            firstname = None
                
                # Sometimes there are unwanted prefixes
                # So we re.search instead of re.match
                match = re.search(r'\d:\d\d[,.]\d\d', word_text)
                if match:
                    line_data['words'].append({
                        'type': 'time',
                        'text': match.group(0),
                        'bbox': word_bbox
                    })
            
            if line_data['words']:
                self.parsed_data.append(line_data)
            surname = None

        return self.parsed_data

    def get_bbox(self, title):
        bbox_match = re.search(r'bbox (\d+ \d+ \d+ \d+)', title)
        if bbox_match:
            return list(map(int, bbox_match.group(1).split()))
        return None
