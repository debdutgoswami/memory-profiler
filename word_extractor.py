from memory_profiler import profile
import requests

class BaseExtractor:
    def __init__(self, url):
        self.url = url

    @profile
    def parse(self):
        response = requests.get(self.url).text
        with open('words.txt', 'w') as f:
            f.writelines(response)