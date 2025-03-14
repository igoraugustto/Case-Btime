from infrastructure.amazon_scraper import AmazonScraper

class ScrapeAmazon:
    def __init__(self):  
        self.scraper = AmazonScraper()

    def execute(self, url: str):
        return self.scraper.scrape(url)
