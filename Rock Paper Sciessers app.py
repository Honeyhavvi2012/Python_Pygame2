import tkinter as tk
import random

def play(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(
        text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}"
    )

root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")  

label = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16))
label.pack(pady=20)

btn_rock = tk.Button(root, text="Rock", width=15, command=lambda: play("rock"))
btn_paper = tk.Button(root, text="Paper", width=15, command=lambda: play("paper"))
btn_scissors = tk.Button(root, text="Scissors", width=15, command=lambda: play("scissors"))

btn_rock.pack(pady=5)
btn_paper.pack(pady=5)
btn_scissors.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=20)

root.mainloop()
