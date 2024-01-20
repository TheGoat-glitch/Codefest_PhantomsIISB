import tkinter as tk
from tkinter import messagebox

class BudgetGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Budgeting Minigame")
        self.master.geometry("400x300")

        self.budget = {"Income": 0, "Expenses": {"Needs": 0, "Wants": 0, "Savings": 0}}
        self.current_level = 1

        self.create_widgets()

    def create_widgets(self):
        self.label_header = tk.Label(self.master, text="Budgeting Minigame", font=("Helvetica", 16))
        self.label_header.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_instruction = tk.Label(self.master, text="Level 1: Differentiate between Needs and Wants")
        self.label_instruction.grid(row=1, column=0, columnspan=2, pady=5)

        self.button_needs = tk.Button(self.master, text="Needs", command=lambda: self.check_answer("Needs"))
        self.button_needs.grid(row=2, column=0, padx=10, pady=5)

        self.button_wants = tk.Button(self.master, text="Wants", command=lambda: self.check_answer("Wants"))
        self.button_wants.grid(row=2, column=1, padx=10, pady=5)

        self.label_progress = tk.Label(self.master, text="Level 1 of 3")
        self.label_progress.grid(row=3, column=0, columnspan=2, pady=5)

        self.button_next = tk.Button(self.master, text="Next Level", state=tk.DISABLED, command=self.next_level)
        self.button_next.grid(row=4, column=0, columnspan=2, pady=10)

    def start_level(self):
        from tkinter import messagebox

class BudgetGame:
    def start_level(self):

        level_scenarios = {
            1: "Differentiate between Needs and Wants",
            2: "Allocate your income to different expense categories",
            3: "Create a budget template for your monthly expenses"
        }

        self.label_instruction.config(text=f"Level {self.current_level}: {level_scenarios[self.current_level]}")


        self.button_needs["state"] = tk.NORMAL
        self.button_wants["state"] = tk.NORMAL


        self.label_progress.config(text=f"Level {self.current_level} of 3")


        self.button_next["state"] = tk.DISABLED

    def check_answer(self, choice):
        from tkinter import messagebox

class BudgetGame:
    def check_answer(self, user_response):
   
        self.button_needs["state"] = tk.DISABLED
        self.button_wants["state"] = tk.DISABLED

     
        correct_answers = {
            1: "Needs",
            2: "Allocate your income to different expense categories",  
            3: "Create a budget template for your monthly expenses"  
        }

        if user_response == correct_answers[self.current_level]:
            messagebox.showinfo("Correct!", "Well done! You answered correctly.")
            self.button_next["state"] = tk.NORMAL 
        else:
            messagebox.showerror("Incorrect", "Oops! That's not the correct answer. Try again.")


    def next_level(self):

        pass

    def show_results(self):

        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetGame(root)
    root.mainloop()
