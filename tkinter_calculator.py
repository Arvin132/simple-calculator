from tkinter import *
from turtle import window_width

root = Tk()
root.title("simple calcualtor")
root.iconbitmap("Oxygen-Icons.org-Oxygen-Apps-accessories-calculator.ico")

input_box = Entry(root,text= "waiting for input", width = 40, borderwidth= 10, bg= "#ADD8E6")
input_box.grid(row= 0, column= 0, columnspan= 5)

total_sum = 0

def button_func(x):
    return lambda : input_box.insert(END, str(x))

key_n = 1
for j in range(3):
    for i in range(3):
        temp = Button(root, text = str(key_n), width= 10, pady= 10, command= button_func(key_n))
        temp.grid(row= j + 1, column= i % 3)
        key_n += 1

def plus_func():
    temp = input_box.get()
    input_box.delete(0, END)
    global total_sum
    total_sum += int(temp)
    status = Label(root,text= f"current number = {total_sum}", relief= SUNKEN)
    status.grid(row = 5, sticky= E)
    

def equal_func():
    temp = input_box.get()
    if (temp == ""):
        temp = 0
    input_box.delete(0, END)
    global total_sum
    input_box.insert(0, total_sum + int(temp))
    total_sum = 0
    status = Label(root,text= f"current number = {total_sum}", relief= SUNKEN)
    status.grid(row = 5, sticky= E)
    

def clear_func():
    global total_sum
    total_sum = 0
    input_box.delete(0, END)
    status = Label(root,text= f"current number = {total_sum}", relief= SUNKEN)
    status.grid(row = 5, sticky= E)
    


plus_sign = Button(root, text = '+',width= 10,height= 3, pady= 20, command= plus_func)
eq_sign = Button(root, text = '=',width= 10, pady= 10, command = equal_func)
b0 = Button(root, text = str(0), width= 20, pady= 10, command= button_func(0))
bclear = Button(root, text = 'clear', width= 20, pady= 10, command= clear_func)

plus_sign.grid(row= 1, column=4, rowspan= 2)
eq_sign.grid(row = 3, column= 4)
b0.grid(row = 4, column= 0, columnspan= 2)
bclear.grid(row = 4, column= 2, columnspan= 3)

status = Label(root,text= f"current number = {total_sum}",bd = 2, width = 20, relief= SUNKEN)
status.grid(row = 5, column=0, columnspan= 4, sticky= E)



root.mainloop()
