class MarginalUtilityProduct:
    def __init__(self, name: str, mu_per_price_list: list[float], price: float):
        self.name = name
        self.mu_per_price_list = mu_per_price_list
        self.price = price
        self.quantity = 0

    def add_quantity(self, quantity = 1):
        self.quantity = self.quantity + quantity

    def get_mu_per_price(self) -> float:
        quantity = self.quantity if self.quantity > 0 else 1 
        return self.mu_per_price_list[quantity]
    
    def gross(self) -> float:
        return self.quantity * self.price
