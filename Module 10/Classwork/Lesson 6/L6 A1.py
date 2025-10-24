from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='lightblue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload = Image.open('img.jpg')
# Resize the image using resize() method
upload = upload.resize((300, 300))
# Convert this image to Tkinter compatible image
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='blue')
label.place(x=180, y=20)

label1 = Label(root,
               text = 'Hey User! Welcome to Denomination Counter Application.',
               bg='lightblue',)
label1.place(x=180, y=340)

# Function to display a message box and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        'Alert', 'Do you want to calculate the denomination count?')
    if MsgBox == 'ok':
        topwin()

# Adding Buttons to the main window
button1 = Button(root,
                 text = "Let's get started",
                 command = msg,
                 bg='brown',
                 fg='white')
button1.place(x=260, y=360)

# Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg='light grey')
    top.geometry('600x350')

    label = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="200", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            n2000 = amount // 2000 #3400 // 2000 = 1
            amount %= 2000         #3400 % 2000 = 140
            n500 = amount // 500
            amount %= 500
            n100 = amount // 100

            t1.delete(0, END) #This deletes everything from index 0 (start) to END (last character)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(n2000))
            t2.insert(END, str(n500))
            t3.insert(END, str(n100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text="Calculate", command=calculator, bg='brown', fg='white')

    # Centering Widgets in the Top Window
    label.place(x=200, y=50)
    entry.place(x=200, y=80)
    lbl.place(x=140, y=170)
    btn.place(x=240, y=120)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()