import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"The product is: {product}")
    except ValueError:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Please enter valid numbers.")


window = tk.Tk()
window.geometry("400x300")
window.title("Getting Started with Widgets")


desc_label = tk.Label(window, text="This application calculates the product of two numbers.")
desc_label.pack(pady=5)

label1 = tk.Label(window, text="Enter first number:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack(pady=5)

label2 = tk.Label(window, text="Enter second number:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack(pady=5)

calc_button = tk.Button(window, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=10)

result_box = tk.Text(window, height=3, width=40)
result_box.pack(pady=10)