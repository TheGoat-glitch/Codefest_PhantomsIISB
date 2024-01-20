import tkinter as tk
from tkinter import messagebox
import random

class BudgetGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Budgeting Minigame")
        self.master.geometry("400x300")

        self.setup_game()

    def setup_game(self):
        self.budget = {"Income": 0, "Expenses": {"Needs": 0, "Wants": 0, "Savings": 0}}
        self.current_level = 1
        self.score = 0
        self.level_scenarios = self.generate_scenarios()
        self.create_widgets()
        self.start_level()

    def create_widgets(self):
        self.label_header = tk.Label(self.master, text="Budgeting Minigame", font=("Helvetica", 16, "bold"))
        self.label_header.grid(row=0, column=0, columnspan=3, pady=10)

        self.label_instruction = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.label_instruction.grid(row=1, column=0, columnspan=3, pady=5)

        self.label_score = tk.Label(self.master, text=f"Score: {self.score}", font=("Helvetica", 12))
        self.label_score.grid(row=4, column=0, pady=5)

        self.label_progress = tk.Label(self.master, text=f"Level {self.current_level} of {len(self.level_scenarios)}", font=("Helvetica", 12))
        self.label_progress.grid(row=4, column=1, pady=5)

        self.button_next = tk.Button(self.master, text="Next Level", state=tk.DISABLED, command=self.next_level)
        self.button_next.grid(row=4, column=2, pady=10)

        self.init_level_ui()

    def init_level_ui(self):
        if self.current_level == 1:
            self.button_needs = tk.Button(self.master, text="Needs", command=lambda: self.check_answer("Needs"))
            self.button_needs.grid(row=2, column=0, padx=10, pady=5)

            self.button_wants = tk.Button(self.master, text="Wants", command=lambda: self.check_answer("Wants"))
            self.button_wants.grid(row=2, column=1, padx=10, pady=5)
        # Add similar logic for other levels

    def generate_scenarios(self):
        scenarios = {
            1: {"description": "Differentiate between Needs and Wants",
                "options": ["Needs", "Wants"],
                "correct_answer": random.choice(["Needs", "Wants"])},
            2: {"description": "Allocate your income to different expense categories",
                "options": ["Rent", "Entertainment", "Savings"],
                "correct_answer": "Rent"},
            3: {"description": "Create a budget template for your monthly expenses",
                "options": ["Fixed", "Variable", "Discretionary"],
                "correct_answer": "Fixed"}
        }
        return scenarios

    def start_level(self):
        level_scenario = self.level_scenarios[self.current_level]
        self.label_instruction.config(text=f"Level {self.current_level}: {level_scenario['description']}")
        self.init_level_ui()
        self.reset_ui_for_new_level()
        self.label_progress.config(text=f"Level {self.current_level} of {len(self.level_scenarios)}")

    def reset_ui_for_new_level(self):
        self.button_needs["state"] = tk.NORMAL
        self.button_wants["state"] = tk.NORMAL
        self.button_next["state"] = tk.DISABLED

    def check_answer(self, user_response):
        correct_answer = self.level_scenarios[self.current_level]["correct_answer"]
        self.button_needs["state"] = tk.DISABLED
        self.button_wants["state"] = tk.DISABLED

        if user_response == correct_answer:
            self.score += 50
            self.label_score.config(text=f"Score: {self.score}")
            messagebox.showinfo("Correct!", "Well done! You answered correctly.")
            if self.current_level < len(self.level_scenarios):
                self.button_next["state"] = tk.NORMAL
        else:
            messagebox.showerror("Incorrect", "Oops! That's not the correct answer. Try again.")

    def next_level(self):
        self.current_level += 1
        if self.current_level > len(self.level_scenarios):
            self.show_results()
        else:
            self.start_level()

    def calculate_score(self):
        return self.score

    def show_results(self):
        final_score = self.calculate_score()
        messagebox.showinfo("Game Over", f"Congratulations! You completed all levels.\nYour final score: {final_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetGame(root)
    root.mainloop()
