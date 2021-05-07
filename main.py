# Exercise 2
# Temperature Converter
# Fahrenheit to Celsius and Celsius to Fahrenheit

import tkinter as tk
from tkinter import LabelFrame, Button, Entry, END, messagebox,INSERT

window = tk.Tk()
window.geometry("600x400")  # window size
window.title("Temperature Converter F to C / C to F")
window.config(bg="black")

lblfc_to_f = tk.LabelFrame(window, text="Celsius to Fahrenheit", bg="orange")
lblfc_to_f.place(x=50, y=60, height=100, width=180)
lblff_to_c = tk.LabelFrame(window, text="Fahrenheit to Celsius", bg="orange")
lblff_to_c.place(x=300, y=60, height=100, width=180)
e_celsius = tk.Entry(lblfc_to_f, state="readonly")  # execution of this program the entry is readonly
e_celsius.place(x=40, y=20, width=100)
e_fahrenheit = tk.Entry(lblff_to_c, state="readonly")
e_fahrenheit.place(x=40, y=20, width=100)
conversion = tk.Entry(window, state="readonly")  # execution of this program the entry is readonly
conversion.place(x=170, y=300, height=50, width=200)


def convert(): # function defined to be called when convert button is pushed
    try:
        if e_celsius['state'] == "normal":  # if state of entry changes to normal then activate the following:
            convert1 = int(e_celsius.get()) * 1.8 + 32  # conversion from celsius to fahrenheit
            conversion.config(
            state="normal")  # changing conversion entry where output will be displayed into normal state and not readonly
            conversion.insert(INSERT, str(round(convert1, 1)))  # inserting converted value into the output entry
    except:
        messagebox.showinfo("ERROR", "Must be numbers")
    try:
        if e_fahrenheit['state'] == "normal":
            convert2 = (int(e_fahrenheit.get()) - 32) * (5 / 9)
            conversion.config(state="normal")
            conversion.insert(INSERT, str(round(convert2, 1)))
    except:
        messagebox.showinfo("ERROR", "Must be numbers")


def activate1():  # function defined to change states of entries when buttons are pushed
    e_celsius.config(state="normal")
    e_fahrenheit.config(state="readonly")


btnactivate = tk.Button(window, text="Activate- C to F",
                        command=activate1, bg="orange", borderwidth=7)  # calls function that activates celsius entry
btnactivate.place(x=70, y=180)


def activate2():  # function defined to change states of entries when buttons are pushed
    e_fahrenheit.config(state="normal")
    e_celsius.config(state="readonly")


btnactivate2 = tk.Button(window, text="Activate- F to C",
                         command=activate2, bg="orange", borderwidth=7)  # calls function that activates fahrenheit entry
btnactivate2.place(x=320, y=180)

btnConv = tk.Button(window, text="Calculate Conversion", command=convert, bg="orange", borderwidth=7)  # calls function that converts entries
btnConv.place(x=190, y=250)


def clear():  # defining function for the clear button
    e_fahrenheit.delete(0, tk.END)
    e_celsius.delete(0, tk.END)
    conversion.delete(0, tk.END)


btnclear = tk.Button(window, text="Clear", command=clear, bg="orange", borderwidth=7)  # clear function being called
btnclear.place(x=470, y=300)


def exit():
    msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application", icon='warning')
    if msg_box == "yes":
        window.destroy()
    else:
        messagebox.showinfo("Return", "You will now return to the App", icon="warning")

btnexit = tk.Button(window, text="Exit Program", command=exit, bg="orange", borderwidth=7)
btnexit.place(x=450, y=350)

window.mainloop()
