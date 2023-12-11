from ipaddress import collapse_addresses
from tkinter import *

from numpy import pad



window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=25, pady=15)

def convert():
    # 1 Mile = 1.609344 Kilometers
    km = 1.609344
    n_to_convert = int(user_input.get())
    conversion = round(n_to_convert * km)
    c_number.configure(text=conversion)


#user input
user_input = Entry(width=15)
user_input.grid(column=1, row=0)

#text on screen
w_text = Label(text="is equal to")
w_text.grid(column=0, row=1)

m_label = Label(text="Miles")
m_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

c_number = Label(text="0")
c_number.grid(column=1, row=1)

#calculate button
c_button = Button(text="Calculate", command=convert)
c_button.grid(column=1, row=2)


window.mainloop()