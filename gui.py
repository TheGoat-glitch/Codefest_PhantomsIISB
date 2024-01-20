import tkinter as tk
from tkinter import messagebox, simpledialog
from user_manager import UserManager
from stock_manager import StockManager
from investment_manager import InvestmentManager
import update_price
import display_news
import exit

class StockMarketApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stock Market Simulation Game")
        self.geometry("800x600")

        self.user_manager = UserManager()
        self.stock_manager = StockManager()
        self.investment_manager = InvestmentManager(self.stock_manager)

        self.create_login_widgets()
        self.create_action_buttons()

    def create_login_widgets(self):
        login_frame = tk.Frame(self)
        login_frame.pack(side=tk.TOP, anchor='nw', padx=10, pady=10)

        tk.Label(login_frame, text="Username:").pack(side=tk.LEFT)
        self.username_entry = tk.Entry(login_frame)
        self.username_entry.pack(side=tk.LEFT)

        tk.Label(login_frame, text="Password:").pack(side=tk.LEFT)
        self.password_entry = tk.Entry(login_frame, show='*')
        self.password_entry.pack(side=tk.LEFT)

        tk.Button(login_frame, text="Login", command=self.login).pack(side=tk.LEFT)
        tk.Button(login_frame, text="Register", command=self.register).pack(side=tk.LEFT)

    def create_action_buttons(self):
        action_frame = tk.Frame(self)
        action_frame.pack(pady=10)

        tk.Button(action_frame, text="View Firms", command=self.view_firms).pack(side=tk.LEFT)
        tk.Button(action_frame, text="Invest", command=self.invest).pack(side=tk.LEFT)
        tk.Button(action_frame, text="Track Revenue", command=self.track_revenue).pack(side=tk.LEFT)
        tk.Button(action_frame, text="Update Stock Prices", command=self.update_prices).pack(side=tk.LEFT)
        tk.Button(action_frame, text="Display Market News", command=self.show_news).pack(side=tk.LEFT)
        tk.Button(action_frame, text="Exit", command=self.exit_application).pack(side=tk.LEFT)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = self.user_manager.login_user(username, password)
        messagebox.showinfo("Login", message)
        if success:
            self.update_login_status(username)

    def register(self):
        username = simpledialog.askstring("Register", "Enter new username:")
        password = simpledialog.askstring("Register", "Enter new password:", show='*')
        if username and password:
            success, message = self.user_manager.register_user(username, password)
            messagebox.showinfo("Register", message)

    def view_firms(self):
        firms_info = self.stock_manager.get_firms_info()
        messagebox.showinfo("Firms", firms_info)

    def invest(self):
        firm = simpledialog.askstring("Invest", "Enter firm name to invest in:")
        amount = simpledialog.askinteger("Invest", "Enter amount to invest:")
        if firm and amount:
            message = self.investment_manager.handle_investment(firm, amount)
            messagebox.showinfo("Invest", message)

    def track_revenue(self):
        revenue_info = self.investment_manager.track_revenue()
        messagebox.showinfo("Revenue Tracking", revenue_info)

    def update_login_status(self, username):
        login_status_label = tk.Label(self, text=f"Logged in as: {username}")
        login_status_label.pack(pady=10)


    def update_prices(self):
        updated_info = update_price.update_stock_prices(self.stock_manager)
        messagebox.showinfo("Update Prices", updated_info)

    def show_news(self):
        news_info = display_news.display_market_news(self.stock_manager)
        messagebox.showinfo("Market News", news_info)

    def track_revenue(self):
        revenue_info = self.investment_manager.track_revenue()
        messagebox.showinfo("Revenue Tracking", revenue_info)

    def exit_application(self):
        exit.exit_app(self)

    def update_login_status(self, username):
        self.login_status_label = tk.Label(self, text=f"Logged in as: {username}")
        self.login_status_label.pack(pady=10)

if __name__ == "__main__":
    app = StockMarketApp()
    app.mainloop()
