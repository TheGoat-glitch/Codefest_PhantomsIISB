import threading
import yfinance as yf

class StockManager:
    def __init__(self, stock_symbols):
        self.stock_symbols = stock_symbols
        self.firms = {symbol: None for symbol in stock_symbols}

    def update_stock_prices(self, callback=None):
        thread = threading.Thread(target=self._update_prices_thread, args=(callback,))
        thread.start()

    def _update_prices_thread(self, callback):
        try:
            for symbol in self.stock_symbols:
                try:
                    data = yf.download(symbol, period='1d')
                    latest_price = data['Close'].iloc[-1]
                    self.firms[symbol] = latest_price
                except Exception as e:
                    print(f"Error fetching data for {symbol}: {e}")
                self.firms[symbol] = None  
            if callback:
                callback()  
        except Exception as e:
            print(f"Error updating stock prices: {e}")

