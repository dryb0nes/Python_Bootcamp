from tkinter import Tk
from tk_material_design.button import MDBtn

root = Tk()

button = MDBtn(root, text="Click Me", raised=True)
button.pack()

root.mainloop()
