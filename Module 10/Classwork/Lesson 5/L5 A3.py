from tkinter import *

# Setting up Main Window
root = Tk()
root.geometry('400x300')
root.title('main')

# function to open New (Top Level) Window
def topwin():
    # Setting up Top Window
    top = Toplevel()
    top.geometry('180x100')
    top.title('toplevel')
    # Adding a label widget to Top Window
    l2 = Label(top, text='This is a toplevel Window')
    l2.pack()

    top.mainloop()

# Adding a label and button widget to Root (Main) Window
l = Label(root, text='This is Root Window')
btn = Button(root, text = 'Click here to open another window', command=topwin)

# Arranging the widgets
l.pack()
btn.pack()

# Running the main event loop
root.mainloop()