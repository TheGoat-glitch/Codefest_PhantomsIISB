import tkinter as tk
from tkinter import ttk, messagebox
from flask import Flask, render_template, jsonify

class BudgetGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Budgeting Minigame")
        self.master.geometry("800x700")

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.current_level = 1
        self.score = 0
        self.level_scenarios = self.generate_scenarios()

        self.label_header = ttk.Label(self.master, text="Budgeting Minigame", font=("Helvetica", 20, "bold"))
        self.label_header.grid(row=0, column=0, columnspan=3, pady=20)

        self.label_instruction = ttk.Label(self.master, text="", font=("Helvetica", 14))
        self.label_instruction.grid(row=1, column=0, columnspan=3, pady=10)

        self.label_score = ttk.Label(self.master, text=f"Score: {self.score}", font=("Helvetica", 12))
        self.label_score.grid(row=0, column=2, padx=10, pady=5, sticky="e") 

        self.label_progress = ttk.Label(self.master, text="", font=("Helvetica", 12))
        self.label_progress.grid(row=4, column=1, pady=5)

        self.button_next = ttk.Button(self.master, text="Next Level", state=tk.DISABLED, command=self.next_level)
        self.button_next.grid(row=4, column=2, pady=10)

        self.init_level_ui()
        self.start_level()

    def init_level_ui(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, ttk.Button) and widget not in [self.button_next]:
                widget.destroy()

        current_options = self.level_scenarios[self.current_level]["options"]
        for i, option in enumerate(current_options):
            button = ttk.Button(self.master, text=option, command=lambda opt=option: self.check_answer(opt))
            button.grid(row=2 + i, column=0, padx=10, pady=10, sticky='ew')

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

    def start_level(self):
        level_scenario = self.level_scenarios[self.current_level]
        self.label_instruction.config(text=f"Level {self.current_level}: {level_scenario['description']}")
        self.init_level_ui()
        self.label_progress.config(text=f"Level {self.current_level} of {len(self.level_scenarios)}")
        self.button_next["state"] = tk.NORMAL

    def check_answer(self, user_response):
        correct_answer = self.level_scenarios[self.current_level]["correct_answer"]
        if user_response == correct_answer:
            self.score += 50
            self.label_score.config(text=f"Score: {self.score}")
            messagebox.showinfo("Correct!", "Well done! You answered correctly.")
            if self.current_level < len(self.level_scenarios):
                self.button_next["state"] = tk.NORMAL
            else:
                self.button_next.config(text="Finish", command=self.show_results)
        else:
            self.score -= 40  
            self.label_score.config(text=f"Score: {self.score}")
            messagebox.showerror("Incorrect", "Oops! That's not the correct answer. Try again.")

    def next_level(self):
        self.current_level += 1
        if self.current_level > len(self.level_scenarios):
            self.button_next.config(text="Finish", command=self.show_results)
        else:
            self.start_level()

    def show_results(self):
        final_score = self.calculate_score()
        messagebox.showinfo("Game Over", f"Congratulations! You completed all levels.\nYour final score: {final_score}")
        self.master.quit()

    def calculate_score(self):
        return self.score

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetGame(root)
    root.mainloop()