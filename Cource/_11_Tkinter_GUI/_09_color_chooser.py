import tkinter as tk
from tkinter import colorchooser


def handle_color_chooser_click():
    picked_color = (
        colorchooser.askcolor()
    )  # return tuple of ((red,green,blue),'hex_value')
    # we can only apply the hex value to the components
    frame.config(bg=picked_color[1])


frame = tk.Tk()

frame.geometry("500x500")

show_color_chooser_button = tk.Button(
    frame,
    text="show colorchooser",
    font=("monospace", 35),
    command=handle_color_chooser_click,
)
show_color_chooser_button.pack()

frame.mainloop()
