import requests

class MercadoLivreClient:
    def __init__(self):
        self.base_url = "https://api.mercadolibre.com/items/"

    def fetch_product(self, product_id: str):
        url = f"{self.base_url}{product_id}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"❌ Erro ao acessar API do Mercado Livre: {response.status_code}")
            print(f"📌 Resposta da API: {response.text}")  # Depuração
            return None

        data = response.json()
        print("📌 Resposta da API Mercado Livre:", data)  # Verifica o que foi retornado

        if "title" not in data:
            print("⚠️ Produto não encontrado ou API mudou o formato.")
            return None

        return {
            "title": data.get("title", "N/A"),
            "price": data.get("price", "N/A"),
            "available_quantity": data.get("available_quantity", "N/A")
        }
