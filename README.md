# 🕷️ Scrapy - Web Scraping com Python

## Projeto scraping empregos no site "empregos.maringa.com"
O Projeto utiliza o Scrapy para navegar e extrair dados de vagas de emprego no site empregos.maringa.com. Ele faz scraping de múltiplas páginas e coleta os seguintes dados de cada vaga:

- Título da vaga
- Nome da empresa
- Data de publicação
- Link para candidatura

Os dados extraídos são retornados como dicionários e podem ser salvos, por exemplo, em CSV com:

## 📌 O que é o Scrapy?

[Scrapy](https://scrapy.org/) é um framework **open-source em Python** para **extração de dados de websites** de forma rápida, eficiente e estruturada. Com ele, você pode criar spiders (robôs) que navegam e coletam dados automaticamente de páginas da web.

---

## 🚀 Vantagens do Scrapy

- ⚡ Alta performance com suporte a **concorrência**
- ♻️ Reutilização de código com middlewares e pipelines
- 📄 Exportação fácil para CSV, JSON, XML, banco de dados etc.
- 🔧 Estrutura modular e altamente personalizável
- 🕸️ Ideal para projetos pequenos ou grandes de scraping

---

## 🧰 Instalação

### **Recomendado usar um ambiente virtual:**
Na pasta do projeto, digite os seguintes comandos para criar o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate          # Linux/macOS
source .venv\Scripts\activate      # Windows
```
### Instale com pip:
```bash
pip install scrapy
```

## 🗂️ Estrutura de Projeto
Para iniciar um projeto, é necessário digitar o seguinte comando:
```bash
scrapy startproject scarpy_empregos
```

Segue abaixo a estrutura utilizada no projeto:
```bash
scrapy_empregos/
├── .venv/
├── .git/
├── data/ # Local onde os dados serão salvos
├── transformacao/
│   └── main.py # Etapa onde será realizado o tratamento 
                # e filtrado apenas os registros desejados
├── scrapy_empregos/
│   ├── __init__.py
│   ├── items.py         # Define os dados que serão extraídos
│   ├── middlewares.py   # Lógica intermediária da requisição
│   ├── pipelines.py     # Processamento dos dados extraídos
│   ├── settings.py      # Configurações do projeto
│   └── spiders/         # Onde ficam os spiders (robôs)
│       └── empregos.py.py
└── scrapy.cfg

```

### Executar o spider
Para executar o spider, é necessário estar dentro do diretório ```scrapy_empregos/scrapy_empregos``` e executar o seguinte comando:

```bash
scrapy crawl empregos
```

Executar o spider e salvar os resultados em um arquivo json:
```bash
scrapy crawl empregos -O ../data/data.csv
```