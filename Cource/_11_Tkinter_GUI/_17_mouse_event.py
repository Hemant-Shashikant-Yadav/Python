from tkinter import *


def doSomething(event):
    print("Mouse coordinates: " + str(event.x)+","+str(event.y))


window = Tk()

window.bind("<Button-1>", doSomething)

window.bind("<Button-3>", doSomething)

window.bind("<ButtonRelease>", doSomething)

# window.bind("<Leave>" doSomething)

# window.bind("<Enter>", doSomething)

# window.bind("<Motion>", doSomething)  # Where the mouse moved

window.mainloop()
