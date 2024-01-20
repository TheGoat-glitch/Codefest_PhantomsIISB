class InvestmentManager:
    def __init__(self, stock_manager):
        self.stock_manager = stock_manager
        self.portfolio = {}
        self.initial_balance = 1000
        self.balance = self.initial_balance

    def handle_investment(self, firm, amount):
        if firm not in self.stock_manager.firms or amount > self.balance:
            return "Invalid investment."

        shares = amount / self.stock_manager.firms[firm]
        self.portfolio[firm] = self.portfolio.get(firm, 0) + shares
        self.balance -= amount
        return f"Invested ${amount} in {firm}. Total shares: {self.portfolio[firm]:.2f}"

    def calculate_profit_loss(self):
        total_value = sum(self.stock_manager.firms[firm] * shares for firm, shares in self.portfolio.items())
        return total_value - self.initial_balance

    def track_revenue(self):
        profit_loss = self.calculate_profit_loss()
        if self.balance <= 0:
            if profit_loss > 0:
                self.balance += profit_loss
                return f"Profit added to balance. New balance: ${self.balance:.2f}"
            else:
                return "You're in debt."
        return f"Current Balance: ${self.balance:.2f}\nProfit/Loss: ${profit_loss:.2f}"
