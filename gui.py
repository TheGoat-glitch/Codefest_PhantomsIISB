import tkinter as tk
from tkinter import messagebox, simpledialog, font
from PIL import Image, ImageTk
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
        self.set_background_image('stock.jpg')

        self.user_manager = UserManager()
        self.stock_manager = StockManager()
        self.investment_manager = InvestmentManager(self.stock_manager)

        self.create_login_widgets()
        self.create_action_buttons()
        self.status_label = tk.Label(self, text="Data not saved", fg="red", font=('Helvetica', 20))
        self.status_label.place(relx=1.0, rely=0.0, anchor='ne')

    def set_background_image(self, image_file):
        self.background_image = Image.open(image_file)
        self.background_image = self.background_image.resize((800, 600), Image.Resampling.LANCZOS)  
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        background_label = tk.Label(self, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = self.background_photo

    def create_login_widgets(self):
        login_frame = tk.Frame(self)
        login_frame.pack(pady=10)

        entry_frame = tk.Frame(login_frame)
        entry_frame.pack(side=tk.TOP, fill='x')

        self.username_entry = tk.Entry(entry_frame, width=20)
        self.username_entry.pack(side=tk.TOP, padx=5)

        self.password_entry = tk.Entry(entry_frame, show='*', width=20)
        self.password_entry.pack(side=tk.TOP, padx=5)

        button_frame = tk.Frame(login_frame)
        button_frame.pack(side=tk.TOP, fill='x')

        button_style = {'bg': 'green', 'padx': 5, 'pady': 5}
        tk.Button(button_frame, text="Login", command=self.login, **button_style).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Register", command=self.register, **button_style).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Logout", command=self.logout, **button_style).pack(side=tk.LEFT, padx=5)

    def create_action_buttons(self):
        action_frame = tk.Frame(self)
        action_frame.pack(pady=10)
        button_style = {'bg': 'green', 'padx': 5, 'pady': 5}
        tk.Button(action_frame, text="Sell Shares", command=self.sell_shares, **button_style).pack(side=tk.TOP, fill='x', pady=5)
        tk.Button(action_frame, text="View Shares", command=self.view_sales, **button_style).pack(side=tk.TOP, fill='x', pady=5)
        tk.Button(action_frame, text="View Firms", command=self.view_firms, **button_style).pack(side=tk.TOP, fill='x', pady=5)
        tk.Button(action_frame, text="Invest", command=self.invest, **button_style).pack(side=tk.TOP, fill='x', pady=5)
        tk.Button(action_frame, text="Track Revenue", command=self.track_revenue, **button_style).pack(side=tk.TOP, fill='x', pady=5)
        tk.Button(action_frame, text="Update Stock Prices", command=self.update_prices, **button_style).pack(side=tk.TOP, fill='x', pady=5)
        tk.Button(action_frame, text="Display Market News", command=self.show_news, **button_style).pack(side=tk.TOP, fill='x', pady=5)
        tk.Button(action_frame, text="Exit", command=self.exit_application, **button_style).pack(side=tk.TOP, fill='x', pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = self.user_manager.login_user(username, password)
        messagebox.showinfo("Login", message)
        if success:
            self.update_login_status(username)
            self.password_entry.delete(0, tk.END)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            success, message = self.user_manager.register_user(username, password)
            messagebox.showinfo("Register", message)
            if success:
                self.password_entry.delete(0, tk.END)

    def logout(self):
        self.user_manager.current_user = None
        self.update_login_status(None)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def update_login_status(self, username):
        if username:
            self.status_label.config(text=f"Logged in as: {username}", fg="black")
        else:
            self.status_label.config(text="Data not saved", fg="red")

    def view_firms(self):
        firms_info = self.stock_manager.get_firms_info()
        messagebox.showinfo("Firms", firms_info)

    def sell_shares(self):
        firm = simpledialog.askstring("Sell Shares", "Enter firm name to sell shares:")
        shares = simpledialog.askinteger("Sell Shares", "Enter number of shares to sell:")
        if firm and shares is not None:
            message = self.investment_manager.sell_shares(firm, shares)
            messagebox.showinfo("Sell Shares", message)

    def invest(self):
        firm = simpledialog.askstring("Invest", "Enter firm name to invest in:")
        amount = simpledialog.askinteger("Invest", "Enter amount to invest:")
        if firm and amount:
            message = self.investment_manager.handle_investment(firm, amount)
            messagebox.showinfo("Invest", message)

    def sell_shares(self):
        firm = simpledialog.askstring("Sell Shares", "Enter firm name to sell shares from:")
        shares = simpledialog.askinteger("Sell Shares", "Enter number of shares to sell:")
        if firm and shares is not None:
            message = self.investment_manager.sell_shares(firm, shares)
            messagebox.showinfo("Sell Shares", message)

    def track_revenue(self):
        revenue_info = self.investment_manager.track_revenue()
        messagebox.showinfo("Revenue Tracking", revenue_info)

    def update_prices(self):
        updated_info = update_price.update_stock_prices(self.stock_manager)
        messagebox.showinfo("Update Prices", updated_info)

    def show_news(self):
        news_info = display_news.display_market_news(self.stock_manager)
        messagebox.showinfo("Market News", news_info)

    def view_sales(self):
        portfolio_info = self.investment_manager.get_portfolio_info()
        messagebox.showinfo("Your Portfolio", portfolio_info)

    def exit_application(self):
        exit.exit_app(self)

if __name__ == "__main__":
    app = StockMarketApp()
    app.mainloop()
