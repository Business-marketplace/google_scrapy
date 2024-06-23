import scrapy

class GoogleSpider(scrapy.Spider):
    name = "google"
    allowed_domains = ["google.com"]
    start_urls = ['https://google.com/search?q=meal+prep+plan+in+texas']
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    def parse(self, response):
        search_div = response.css('div#search')
        if search_div:
            for i in search_div:
                yield {'urls': i.css('a::attr(href)').getall(),
                'title': i.css('h3::text').getall()
                }
        else:
            self.logger.info("No search div found")
