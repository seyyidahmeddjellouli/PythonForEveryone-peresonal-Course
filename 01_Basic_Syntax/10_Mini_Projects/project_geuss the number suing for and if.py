import tkinter as tk
import random

# Initialize game variables
secret_number = random.randint(1, 10)
attempts = 3

def guess_number():
    global attempts
    user_guess = int(entry.get())
    result_label.config(text="")

    if user_guess == secret_number:
        result_label.config(text=f"Congratulations! You've guessed the number ({secret_number})!")
        entry.config(state='disabled')
        submit_button.config(state='disabled')
    elif user_guess < secret_number:
        result_label.config(text="Too low! Try a higher number.")
    else:
        result_label.config(text="Too high! Try a lower number.")

    attempts -= 1
    attempts_label.config(text=f"Attempts remaining: {attempts}")

    if attempts == 0:
        result_label.config(text=f"Sorry, you've run out of attempts. The number was: {secret_number}")
        entry.config(state='disabled')
        submit_button.config(state='disabled')

# Create main window
root = tk.Tk()
root.title("Number Guessing Game")

# Create labels, entry, and button
instructions_label = tk.Label(root, text="Guess the number (between 1 and 10):")
entry = tk.Entry(root)
submit_button = tk.Button(root, text="Submit", command=guess_number)
attempts_label = tk.Label(root, text=f"Attempts remaining: {attempts}")
result_label = tk.Label(root, text="", font=('Helvetica', 12, 'bold'))

# Place widgets in the window
instructions_label.pack(pady=20)
entry.pack(pady=20)
submit_button.pack(pady=20)
attempts_label.pack(pady=20)
result_label.pack(pady=40)

# Run the GUI event loop
root.mainloop()
