from flask import Flask, request, render_template, redirect, url_for, session, flash
from functools import wraps
from user_manager import UserManager
from stock_manager import StockManager
from investment_manager import InvestmentManager
import update_price

app = Flask(__name__)
app.secret_key = 'your_secret_key'

user_manager = UserManager()
stock_manager = StockManager()
investment_manager = InvestmentManager(stock_manager)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash("You need to be logged in to access this page.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def index():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        success, message = user_manager.login_user(username, password)
        if success:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash(message, "danger")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        success, message = user_manager.register_user(username, password)
        if success:
            flash(message, "success")
            return redirect(url_for('login'))
        else:
            flash(message, "danger")
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.", "success")
    return redirect(url_for('login'))

@app.route('/view_firms')
@login_required
def view_firms():
    firms_info = stock_manager.get_firms_info()
    return render_template('firms_info.html', firms_info=firms_info)

@app.route('/invest', methods=['GET', 'POST'])
@login_required
def invest():
    if request.method == 'POST':
        firm = request.form['firm']
        amount = float(request.form['amount'])
        message = investment_manager.handle_investment(firm, amount)
        flash(message, "info")
    return render_template('invest.html')

@app.route('/sell_shares', methods=['GET', 'POST'])
@login_required
def sell_shares():
    if request.method == 'POST':
        firm = request.form['firm']
        shares = int(request.form['shares'])
        message = investment_manager.sell_shares(firm, shares)
        flash(message, "info")
    return render_template('sell_shares.html')

@app.route('/view_portfolio')
@login_required
def view_portfolio():
    portfolio_info = investment_manager.get_portfolio_info()
    return render_template('portfolio.html', portfolio_info=portfolio_info)

@app.route('/track_revenue')
@login_required
def track_revenue():
    revenue_info = investment_manager.track_revenue()
    return render_template('track_revenue.html', revenue_info=revenue_info)

@app.route('/update_prices')
@login_required
def update_prices():
    updated_info = update_price.update_stock_prices(stock_manager)
    flash(updated_info, "info")
    return redirect(url_for('index'))

@app.route('/display_news')
@login_required
def display_news():
    news_info = display_news.display_market_news(stock_manager)
    return render_template('market_news.html', news_info=news_info)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
