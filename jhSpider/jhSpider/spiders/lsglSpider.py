import scrapy


class LsglspiderSpider(scrapy.Spider):
    name = 'lsglSpider'
    allowed_domains = ['lsgl.sft.zj.gov.cn', 'oauth.zjzwfw.gov.cn']
    start_urls = ['http://lsgl.sft.zj.gov.cn/']

    def parse(self, response):
        filename = "index.html"
        open(filename, 'w').write(response.body)
