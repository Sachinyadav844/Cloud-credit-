import tkinter as tk
from tkinter import messagebox
import random

# Function to generate a random number
def generate_number():
    return random.randint(1, 100)

# Function to handle the guess
def check_guess():
    try:
        user_guess = int(entry_guess.get())
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number.")
        return
    
    if user_guess < 1 or user_guess > 100:
        messagebox.showwarning("Range Error", "Please guess a number between 1 and 100.")
        return
    
    if user_guess < number_to_guess:
        label_feedback.config(text="Too Low! Try again.")
    elif user_guess > number_to_guess:
        label_feedback.config(text="Too High! Try again.")
    else:
        label_feedback.config(text="Correct! You've guessed the number!")
        messagebox.showinfo("You Won!", "Congratulations! You guessed the number!")
        reset_game()

# Function to reset the game
def reset_game():
    global number_to_guess
    number_to_guess = generate_number()
    label_feedback.config(text="Enter your guess (1-100):")
    entry_guess.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("400x300")

# Generate the random number
number_to_guess = generate_number()

# Create the widgets
label_instruction = tk.Label(root, text="Guess the number between 1 and 100", font=("Helvetica", 14))
label_instruction.pack(pady=20)

entry_guess = tk.Entry(root, font=("Helvetica", 14))
entry_guess.pack(pady=10)

button_check = tk.Button(root, text="Check Guess", font=("Helvetica", 12), command=check_guess)
button_check.pack(pady=10)

label_feedback = tk.Label(root, text="Enter your guess (1-100):", font=("Helvetica", 12))
label_feedback.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
