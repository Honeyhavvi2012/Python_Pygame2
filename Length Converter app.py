import tkinter as tk
from tkinter import ttk

def convert_length():
    try:
        value = float(entry_value.get())
        unit = combo_units.get()

        if unit == "cm to m":
            result = value / 100
        elif unit == "m to cm":
            result = value * 100
        elif unit == "km to m":
            result = value * 1000
        elif unit == "m to km":
            result = value / 1000
        else:
            result = "Invalid conversion"

        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Please enter a valid number!")


root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")
root.configure(bg="#EAF6F6") 

label_heading = tk.Label(root, text="Length Converter", 
                         font=("Arial", 16, "bold"), 
                         bg="#EAF6F6", fg="#008080")
label_heading.pack(pady=20)

frame_entry = tk.Frame(root, bg="#EAF6F6")
frame_entry.pack(pady=10)

tk.Label(frame_entry, text="Enter value:", font=("Arial", 12), 
         bg="#EAF6F6", fg="#004d4d").grid(row=0, column=0, padx=10)
entry_value = tk.Entry(frame_entry, width=15, font=("Arial", 12), bd=3, relief="ridge")
entry_value.grid(row=0, column=1, padx=10)

tk.Label(root, text="Select conversion:", font=("Arial", 12), 
         bg="#EAF6F6", fg="#004d4d").pack(pady=5)

combo_units = ttk.Combobox(root, values=["cm to m", "m to cm", "km to m", "m to km"], font=("Arial", 12))
combo_units.pack(pady=5)
combo_units.current(0)

btn_convert = tk.Button(root, text="Convert", font=("Arial", 12, "bold"),
                        bg="#008080", fg="white", width=12, command=convert_length)
btn_convert.pack(pady=15)

label_result = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), 
                        bg="#EAF6F6", fg="#006666")
label_result.pack(pady=20)

root.mainloop()
