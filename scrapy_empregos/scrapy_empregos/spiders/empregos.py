import scrapy
import pandas as pd

class EmpregosSpider(scrapy.Spider):
    name = "empregos"
    allowed_domains = ["empregos.maringa.com"]
    start_urls = ["https://empregos.maringa.com/"]
    pagina_atual = 1
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
        
        # Encontra o link da próxima página de forma mais robusta
        next_page = response.css('a.page-link.rounded[rel="next"]::attr(href)').get()
        
        if next_page and self.pagina_atual < self.ultima_pagina:
            self.pagina_atual += 1
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

#scrapy crawl empregos -O ../data/data.jsonl