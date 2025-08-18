import tkinter as tk

def calculate_interest():
    try:
        p = float(principle_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())
        
        si = (p * t * r) / 100
        ci = p * ((1 + r/100) ** t - 1)
        
        si_label.config(text=f"Simple Interest: {si:.2f}")
        ci_label.config(text=f"Compound Interest: {ci:.2f}")
    except:
        si_label.config(text="Please enter valid numbers!")
        ci_label.config(text="")

root = tk.Tk()
root.geometry("400x400")
root.title("Age Calculator App")

tk.Label(root, text="Principle:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
principle_entry = tk.Entry(root)
principle_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Time (years):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Rate (%):").grid(row=2, column=0, padx=10, pady=10, sticky="e")
rate_entry = tk.Entry(root)
rate_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Calculate", command=calculate_interest).grid(row=3, column=1, pady=15)

si_label = tk.Label(root, text="Simple Interest: ")
si_label.grid(row=4, column=1, pady=5)

ci_label = tk.Label(root, text="Compound Interest: ")
ci_label.grid(row=5, column=1, pady=5)

root.mainloop()