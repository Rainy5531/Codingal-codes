from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.geometry('200x200')

'''
Function for Displaying Warning Message
This will be called once the button is clicked
messagebox.showwarning('Window Name', 'Message to be displayed')
'''
def msg():
    messagebox.showwarning('Alert', 'Stop! Virus Found.')

# Adding Button Widger to Window
button = Button(root, text='Scan for Virus', command=msg)
button.place(x=50, y=80)

# entering main event logo
root.mainloop()