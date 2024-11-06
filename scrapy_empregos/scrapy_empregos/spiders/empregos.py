import scrapy
import pandas as pd

class EmpregosSpider(scrapy.Spider):
    name = "empregos"
    allowed_domains = ["empregos.maringa.com"]
    start_urls = ["https://empregos.maringa.com/?vagas-de-emprego=1"]
    pagina_atual = 1,
    ultima_pagina = 10

    def parse(self, response):
        empregos = response.css("div.card.card-anuncio.text-dark.mb-4.shadow")
        for emprego in empregos:
            yield {
                "titulo": emprego.css("b.flex-wrap::text").get(),
                "empresa": emprego.css("div.d-none.d-md-block::text").get(),
                "data":  emprego.css("small.text-nowrap.ml-4::text").get(),
                "link": emprego.css("a.btn.mt-3.mt-md-0.curriculo-enviado.w-100.stretched-link.btn-primary::attr(href)").get()
            }
        
        if self.pagina_atual <= self.ultima_pagina:
            next_page = response.css(f"https://empregos.maringa.com/?vagas-de-emprego={self.pagina_atual}")
            if next_page:
                self.pagina_atual += 1
                yield scrapy.Request(url = next_page, callback = self.parse)
#scrapy crawl empregos -O data.csv