from tkinter import *

frame = Tk()
# frame.geometry("400x400")
frame.config(background="maroon")

# name = component(where_to_add, `other properties that can be added later with .config() method too `)
new_label = Label(frame, text="this is label")
new_label.place(x=10, y=20)  # same as setBounds in Swing
# new_label.pack()  # this will automatically set the component to top center of frame and will adjust the frame size such that it will perfectly fit into it, so we don't need to specify place method for it.
new_label.config(
    text="I changed the text of label",
    font=("comic sans MS", 40, "italic"),
    foreground="steelblue",
    background="palegoldenrod",
    relief=RAISED,  # border
    bd=10,
    # padx=10, # adds space between inner content and it's border (up and down)
    # pady=20, # adds space between inner content and it's border (right and left)
)

# creating a image
photo = PhotoImage(file="image.png")
# again calling config method on `new_label` component
new_label.config(
    image=photo,
    compound="top",  # choosing the position of the image with respective to the text or else the image will take over the text even if the text is defined later of defining image
)
new_label.pack()
frame.mainloop()
