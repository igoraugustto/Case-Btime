📌 Descrição do Projeto

Este projeto realiza web scraping de produtos da Amazon utilizando Selenium e coleta dados do Mercado Livre via API oficial. Os dados coletados são salvos em arquivos CSV para posterior análise.



📂 Estrutura do Projeto
│── application
│   ├── use_cases
│   │   ├── scrape_amazon.py  # Web Scraping da Amazon
│   │   ├── fetch_mercadolivre.py  # API do Mercado Livre
│── infrastructure
│   ├── amazon_scraper.py  # Lógica Selenium
│   ├── mercadolivre_client.py  # Cliente para API Mercado Livre
│── domain
│   ├── product.py  # Modelo do Produto
│── main.py  # Ponto de entrada
│── README.md  # Documentação





📦 Instalação



1️⃣ Clonar o repositório

git clone https://github.com/igoraugustto/case-Btime.git
cd scraper_project/src


2️⃣ Criar ambiente virtual (recomendado)

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows


3️⃣ Instalar dependências

pip install -r requirements.txt





🚀 Execução do Projeto

python -m main




📊 Saída Esperada

O projeto salva os dados nos arquivos CSV:

amazon_products.csv (dados coletados via Selenium)

mercadolivre_products.csv (dados coletados via API)





⚙️ Tecnologias Utilizadas

Python 3.10+

Selenium (para scraping da Amazon)

WebDriverManager (para gerenciamento do ChromeDriver)

Requests (para API do Mercado Livre)

CSV (para armazenamento de dados)





🛠 Solução de Problemas

"NoSuchElementException" no Selenium

Verifique se os seletores de elementos HTML estão corretos.

Tente aumentar o tempo de espera com WebDriverWait.

Erro 403 ao acessar API do Mercado Livre

Confirme se o ID do produto está correto.

Caso necessário, gere uma nova chave de API no Mercado Livre.





📜 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para modificar e usar conforme necessário.
