class ViradaCulturalSpider(CrawlSpider):
    name = "virada cultural"
    start_urls = ["http://web.archive.org/web/20160825145532/http://www.viradaculturalpaulista.sp.gov.br/cidades"]

    def parse(self, response):