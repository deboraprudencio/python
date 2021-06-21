from scrapy_cultural_sp.items import Atracao
from scrapy import Spider, Selector, Request
from datetime import datetime, date

class ViradaCulturalSpider(Spider):
    name = "virada cultural"
    start_urls = ["http://web.archive.org/web/20160825145532/http://www.viradaculturalpaulista.sp.gov.br/cidades"]

    def parse(self, response):
        body_sel = Selector(response)
        urls_cidade = body_sel.xpath("//div[@class='list-cities']//ul//li//a/@href").extract()

        for url in urls_cidade:
            yield Request(url, self.parse_atracao) 

    def parse_atracao(self, response):
        body_sel = Selector(response)
        cidade = self.to_str(body_sel.xpath("//h1//text()"))
        endereco = self.to_str(body_sel.xpath("//span[@class='address']//text()"))
        atracao_selectors = body_sel.xpath("//ul[@class='list-events']//li")

        for sel in atracao_selectors:
            atracao = Atracao(cidade=cidade, endereco=endereco)
            atracao["dia"] = self.to_date(sel.xpath(".//span[@class='date']//text()")) # . só aplica o xpath dentro do escopo/trecho do seletor
            atracao["hora"] = self.to_str(sel.xpath(".//span[@class='hour']//text()"))
            atracao["artista"] = self.to_str(sel.xpath(".//span[@class='artist']//text()"))
            
            self.print_item(atracao)

    # Função auxiliar pois extract sempre retorna uma lista
    # Queremos apenas o primeiro elemento em utf-8
    def to_str(self, selector):
        return selector.extract()[0] # .encode("utf-8") é melhor para guardar no bancod e dados

    # Função auxiliar pois a data está em texto na página
    # Queremos guardar em formato de data no banco
    def to_date(self, selector):
        data = self.to_str(selector) # => "14/5"
        dia, mes = data.split("/") # => ["14", "5"]
        ano = date.today().year - 5 # => 2016

        return datetime(ano, int(mes), int(dia)).strftime("%d-%m-%Y")

    def print_item(self, atracao):
        print("hora:", atracao["hora"])
        print("endereco:", atracao["endereco"])
        print("cidade:", atracao["cidade"])
        print("dia:", atracao["dia"])
        print("artista:", atracao["artista"])
        print("--------------------------")