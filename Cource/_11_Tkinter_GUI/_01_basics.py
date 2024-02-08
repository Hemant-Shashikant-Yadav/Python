from tkinter import *

frame = Tk() # same as creating frame
frame.geometry("400x400") # same as setSize
frame.title("This is title") # same as setTitle


# config method is used to apply all the attribute to the given component by giving the named arguments
frame.config(background="palegoldenrod")
frame.mainloop() # same as setVisible
