from tkinter import*
root = Tk()
root.title("My name")
myText = Label(text="Hello my name is",fg="blue",font=20).grid(row=0,column=0)
myText = Label(text="Pupa",fg="green",font=20).grid(row=1,column=1)
myText = Label(text="Thapanapongpaiboon",fg="red",font=20).grid(row=2,column=2)
root.mainloop()