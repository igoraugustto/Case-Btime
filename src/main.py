from application.use_cases.scrape_amazon import ScrapeAmazon
from application.use_cases.fetch_mercadolivre import FetchMercadoLivre
import sys
import os
import csv

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Função para salvar um produto em CSV
def salvar_em_csv(nome_arquivo, produto):
    if produto is None:  # Verifica se produto está vazio
        print(f"⚠️ Erro: Produto inválido. Não foi possível salvar em {nome_arquivo}.")
        return

    with open(nome_arquivo, mode="a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        # Escreve o cabeçalho se o arquivo estiver vazio
        if arquivo.tell() == 0:
            escritor.writerow(["Título", "Preço", "Disponibilidade"])

        # Corrigindo para acessar atributos corretamente
        escritor.writerow([produto.title, produto.price, produto.availability])

if __name__ == "__main__":
    # --- AMAZON SCRAPER ---
    amazon_scraper = ScrapeAmazon()
    amazon_product = amazon_scraper.execute("https://www.amazon.com.br/gp/bestsellers/?ref_=nav_cs_bestsellers")
    print("A coleta do site da Amazon via Selenium gerou esse produto: ", amazon_product)

    # --- MERCADO LIVRE API ---
    ml_scraper = FetchMercadoLivre()
    ml_product = ml_scraper.execute("MLB1919411840")
    print("A coleta do sistema do MERCADO LIVRE via API gerou esse produto: ", ml_product)

    # Salva os produtos nos arquivos CSV
    salvar_em_csv("amazon_products.csv", amazon_product)
    salvar_em_csv("mercadolivre_products.csv", ml_product)

    print("Dados salvos CSV!")
