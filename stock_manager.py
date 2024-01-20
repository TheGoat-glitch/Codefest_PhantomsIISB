import random

class StockManager:
    def __init__(self):
        self.firms = {'FirmA': 100, 'FirmB': 150, 'FirmC': 200}

    def get_firms_info(self):
        return "\n".join(f"{firm}: ${price:.2f}" for firm, price in self.firms.items())

    def update_stock_prices(self):
        for firm in self.firms:
            self.firms[firm] *= random.uniform(0.95, 1.05)
        return self.get_firms_info()
