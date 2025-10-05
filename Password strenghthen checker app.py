import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry.get()
    length = len(password)
    
    if length == 0:
        messagebox.showwarning("Warning", "Please enter a password!")
    elif length < 5:
        result_label.config(text="Password Strength: Weak", fg="red")
    elif length <= 8:
        result_label.config(text="Password Strength: Moderate", fg="orange")
    else:
        result_label.config(text="Password Strength: Strong", fg="green")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")
root.config(bg="#e6f0ff")

tk.Label(root, text="Enter your password:", font=("Arial", 12), bg="#e6f0ff").pack(pady=10)
entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", font=("Arial", 11, "bold"),
                         bg="#4da6ff", fg="white", command=check_strength)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#e6f0ff")
result_label.pack(pady=5)

root.mainloop()