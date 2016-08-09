from tkinter import*


# illustrating basic labels

'''
root = Tk()
theLabel = Label(root, text="Hot dog")
theLabel.pack()
root.mainloop()
'''

# showing button class

'''
root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1")
button2 = Button(topFrame, text="Button 2", fg="orange", bg="black")
button3 = Button(topFrame, text="Button 3", fg="orange")
button4 = Button(bottomFrame, text="Button 4", fg="white", bg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
'''


# expanding on label properties

'''
root = Tk()

one = Label(root, text="one", fg='white', bg='black')
one.pack()
two = Label(root, text="two", fg='orange', bg='purple')
two.pack(fill=X)
three = Label(root, text="three", fg='blue', bg='magenta')
three.pack(fill=Y, side=LEFT)

root.mainloop()
'''