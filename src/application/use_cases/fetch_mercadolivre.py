from infrastructure.mercadolivre_client import MercadoLivreClient

class FetchMercadoLivre:
    def __init__(self):
        self.client = MercadoLivreClient()

    def execute(self, product_id: str):
        return self.client.fetch_product(product_id)
