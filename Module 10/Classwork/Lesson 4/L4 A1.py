from tkinter import *

# create main window
window = Tk()
window.title("Tkinter Sample Window")
window.geometry('300x300')

# Basic widgets
greeting = Label(text = 'Hello User', fg = 'black', bg = 'white')
button = Button(text = 'Click me', fg = 'white', bg = 'black')
entry = Entry(fg = 'white', bg = 'blue', width = 50)

# Display widgets
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master = window, relief = RAISED, borderwidth = 5)
frame.pack()

label = Label(master = frame, text = 'Sample Frame')
label.pack()

textbox = Text(fg = 'green', bg = 'yellow')
textbox.pack()

window.mainloop()