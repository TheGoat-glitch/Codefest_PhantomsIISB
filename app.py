from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# ... other routes if needed ...

if __name__ == '__main__':
    # Serve static files (CSS, JS, images, etc.)
    app.static_folder = 'static'
    
    app.run(debug=True)

