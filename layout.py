from tkinter import *
root = Tk()
entry = Entry()
entry.pack(side=BOTTOM)
listbox = Listbox(root)
listbox.pack()
button = Button(root,text = "send")
button.pack(side=BOTTOM)

root.mainloop()