from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from domain.models import Product

class AmazonScraper:
    def __init__(self):
        options = Options()
        # options.add_argument("--headless") ATENÇÃO! ESTOU DEIXANDO ESTA LINHA COMENTADA POR OPÇÃO MINHA, CASO PREFIRA NÃO VER O ROBÔ "TRABALHANDO" DESCOMENTE ESSA LINHA.
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=options)

    def scrape(self, url: str) -> Product:
        self.driver.get(url)

        try:
            wait = WebDriverWait(self.driver, 10)  # Espera até 10 segundos pelo elemento
            
            title_elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "h2")))
            title = title_elements[1].text.strip() if len(title_elements) > 1 else "N/A"

    # 🔹 Captura o preço (primeiro elemento da lista com a classe específica)
            price_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_cDEzb_p13n-sc-price_3mJ9Z")))
            price = price_elements[0].text.strip() if price_elements else "N/A"


            availability= "0"

        except Exception as e:
            print("Erro ao coletar dados da Amazon:", e)
            title, price, availability = "N/A", "N/A", "N/A"

        self.driver.quit()

        return Product(title=title, price=price, availability=availability)
