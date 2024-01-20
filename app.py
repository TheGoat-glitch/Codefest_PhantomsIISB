from flask import Flask, render_template, request, jsonify
from gui import StockMarketApp

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/minigames')
def minigames():
    return render_template('minigames.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/get_firms_info')
def get_firms_info():
    firms_info = app.stock_market_app.stock_manager.get_firms_info()
    print('Type of firms_info:', type(firms_info))
    return jsonify(firms_info)

if __name__ == '__main__':
    app.stock_market_app = StockMarketApp()
    app.run(debug=True)
