#code is going to convert cm to inches
from tkinter import *
from tkinter import ttk
def calculate(*args):
  try:
    value = float(cm.get())
    inches.set(value/2.54)
  except ValueError:
    pass

root = Tk()
root.title("cm to inches")
# setting up GUI 
mainframe = ttk.Frame(root, padding = "7 7 300 300")
mainframe.grid(column = 0, row = 0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

cm = StringVar()
inches = StringVar()

cm_entry = ttk.Entry(mainframe, width = 7, textvariable = cm)
cm_entry.grid(column = 2, row = 1, sticky=(W, E))

ttk.Label(mainframe, textvariable = inches).grid(column = 2, row= 2, sticky=(W, E))
ttk.Button(mainframe, text = "Calculate", command = calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text ="cm").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text ="is equivalent").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text ="inches").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
  child.grid_configure(padx=5, pady=5)

cm_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()