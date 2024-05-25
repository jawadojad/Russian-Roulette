import random
import tkinter as tk
from tkinter import messagebox

def print_intro():
    messagebox.showinfo("Welcome", "Welcome to Russian Roulette: Programming Edition\n"
                                   "In this game, you'll face a series of Python coding challenges.\n"
                                   "Solve the challenges to 'survive' each round.\n"
                                   "Good luck!")

def start_game():
    print_intro()

    # Initial game setup
    num_rounds = 6  # Number of rounds in the game
    current_round = 1

    # Main game loop
    while current_round <= num_rounds:
        if not run_challenge(current_round):
            break
        current_round += 1

    messagebox.showinfo("Game Over", "Congratulations! You have completed the game.\n"
                                     "Thank you for playing Russian Roulette: Programming Edition.")

def run_challenge(current_round):
    if current_round == 1:
        return challenge_1()
    return True  # Placeholder for additional challenges

def challenge_1():
    root = tk.Tk()
    root.title("Challenge 1")
    
    def check_code():
        user_code = code_input.get("1.0", tk.END)
        try:
            exec(user_code)
            messagebox.showinfo("Result", "Correct! You have survived this round.")
            root.destroy()
            return True
        except Exception as e:
            messagebox.showerror("Result", f"Error: {e}\nIncorrect! You did not survive this round.")
            root.destroy()
            return False

    label = tk.Label(root, text="Challenge 1: Basic Variables and Print Statements\n"
                                "Write a Python program that prints 'Hello, World!' to the console.\n"
                                "Type your code below and press Submit.")
    label.pack()
    
    code_input = tk.Text(root, height=10, width=50)
    code_input.pack()
    
    submit_button = tk.Button(root, text="Submit", command=check_code)
    submit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    start_game()
