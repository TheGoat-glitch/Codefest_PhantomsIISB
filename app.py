from flask import Flask, render_template, request, jsonify, flash
from gui import StockMarketApp
import random

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

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

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/setting')
def setting():
    return render_template('setting.html')

@app.route('/lesson1')
def lesson1():
    return render_template('Category 1.1.html')

@app.route('/lesson2')
def lesson2():
    return render_template('Category 1.2.html')

@app.route('/lesson3')
def lesson3():
    return render_template('Category 1.3.html')

@app.route('/lesson4')
def lesson4():
    return render_template('Category 1.html')

@app.route('/lesson5')
def lesson5():
    return render_template('Category 2.html')

@app.route('/lesson6')
def lesson6():
    return render_template('Category 2.1.html')

@app.route('/lesson7')
def lesson7():
    return render_template('Category 3.html')

@app.route('/lesson8')
def lesson8():
    return render_template('Category 3.html')

@app.route('/lesson9')
def lesson9():
    return render_template('Category 3.1.html')

@app.route('/quiz1')
def quiz1():
    return render_template('Quiz1.html')

@app.route('/quiz2')
def quiz2():
    return render_template('Quiz2.html')

@app.route('/quiz3')
def quiz3():
    return render_template('Quiz3.html')

@app.route('/get_firms_info')
def get_firms_info():
    firms_info = app.stock_market_app.stock_manager.get_firms_info()
    print('Type of firms_info:', type(firms_info))
    return jsonify(firms_info)

class BudgetGame:
    def __init__(self):
        self.current_level = 1
        self.score = 0
        self.level_scenarios = self.generate_scenarios()

    def generate_scenarios(self):
        scenarios = {
            1: {"description": "Is water a need or want?",
                "options": ["Need", "Want"],
                "correct_answer": "Need"},
            2: {"description": "Allocate your income to different expense categories",
                "options": ["Rent", "Entertainment", "Savings"],
                "correct_answer": "Rent"},
            3: {"description": "Create a budget template for your monthly expenses",
                "options": ["Fixed", "Variable", "Discretionary"],
                "correct_answer": "Fixed"}
        }
        return scenarios

    def get_scenario(self):
        if self.current_level <= len(self.level_scenarios):
            scenario = self.level_scenarios[self.current_level]
            return jsonify({
                'description': scenario['description'],
                'options': scenario['options'],
            })
        else:
            return jsonify({'message': 'Game Over'})

    def check_answer(self, user_response):
        correct_answer = self.level_scenarios[self.current_level]["correct_answer"]
        if user_response == correct_answer:
            self.score += 50
            feedback_message = "Well done! You answered correctly."
            enable_next = True
        else:
            self.score -= 40
            feedback_message = "Oops! That's not the correct answer. Try again."
            enable_next = False

        return jsonify({
            'correct': user_response == correct_answer,
            'score': self.score,
            'feedback_message': feedback_message,
            'enable_next': enable_next
        })

    def next_level(self):
        self.current_level += 1
        if self.current_level <= len(self.level_scenarios):
            scenario = self.level_scenarios[self.current_level]
            response = {
                'description': scenario['description'],
                'options': scenario['options'],
                'enable_next': True,
            }
        else:
            response = {'message': 'Game Over', 'enable_next': False, 'options': []}

        return jsonify(response)

budget_game = BudgetGame()

@app.route('/get_scenario')
def get_scenario():
    return budget_game.get_scenario()

@app.route('/check_answer/<user_response>')
def check_answer(user_response):
    return budget_game.check_answer(user_response)

@app.route('/next_level')
def next_level():
    response = budget_game.next_level()
    if 'options' not in response:
        response['options'] = []  # Add an empty list if 'options' is not present

    return response

if __name__ == '__main__':
    app.stock_market_app = StockMarketApp()
    app.run(debug=True)
