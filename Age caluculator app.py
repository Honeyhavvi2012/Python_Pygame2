from tkinter import *
from datetime import date

root = Tk()
root.title('Age Calculator App')
root.geometry('400x400')

lbl1 = Label(root, text="Name", bg="#3895D3", fg='white', width=12)
lbl2 = Label(root, text="Date", bg="#3895D3", fg='white', width=12)
lbl3 = Label(root, text="Month", bg="#3895D3", fg='white', width=12)
lbl4 = Label(root, text="Year", bg="#3895D3", fg='white', width=12)

name_entry = Entry(root)
day_entry = Entry(root)
month_entry = Entry(root)
year_entry = Entry(root)

def display_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        today = date.today()
        age = today.year - year - ((today.month, today.day) < (month, day))

        greet = "Hello " + name
        message = f"\nYou are {age} years old."
        textbox.delete(1.0, END)  
        textbox.insert(END, greet)
        textbox.insert(END, message)
    except:
        textbox.delete(1.0, END)
        textbox.insert(END, "Please enter valid numbers for date, month, and year.")

btn = Button(root, text="Calculate Age", command=display_age, bg="red", fg="white")

textbox = Text(root, bg="#BEBEBE", fg="black", height=4, width=35)

lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)

lbl2.place(x=20, y=60)
day_entry.place(x=150, y=60)

lbl3.place(x=20, y=100)
month_entry.place(x=150, y=100)

lbl4.place(x=20, y=140)
year_entry.place(x=150, y=140)

btn.place(x=130, y=180)
textbox.place(x=20, y=230)

root.mainloop()
