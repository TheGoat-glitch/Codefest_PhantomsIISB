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

    def display_news(self):
        news_events = ["Market Bull Run", "Market Crash", "Stable Market"]
        event = random.choice(news_events)
        news_message = f"News: {event}\n"

        if event == "Market Bull Run":
            for firm in self.firms:
                self.firms[firm] *= 1.1  
            news_message += "Market is experiencing a bull run. Stock prices have increased."
        elif event == "Market Crash":
            for firm in self.firms:
                self.firms[firm] *= 0.9  
            news_message += "Market crash! Stock prices have fallen."
        else:
            news_message += "The market is stable with no significant changes in stock prices."

        return news_message
