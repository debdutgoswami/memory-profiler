from word_extractor import BaseExtractor

if __name__ == "__main__":
    url = input("url: ")
    extractor = BaseExtractor(url)
    extractor.parse()