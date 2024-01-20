from flask import Flask, render_template

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
    
if __name__ == '__main__':
    # Serve static files (CSS, JS, images, etc.)
    app.run(debug=True)

