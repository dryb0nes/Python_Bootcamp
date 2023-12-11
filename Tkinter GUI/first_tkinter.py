from tkinter import *


window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=500)




my_label = Label(text="I'm a label.", font=("Calibri", 20, "bold"))
my_label.grid(column=0, row=0)



def button_clicked():
    input_text = input.get()
    my_label.configure(text=input_text)
    

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)


button = Button(text="Click me 2", command=button_clicked)
button.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()