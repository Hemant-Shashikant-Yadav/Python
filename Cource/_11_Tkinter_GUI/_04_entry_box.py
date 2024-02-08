import tkinter as tk

frame = tk.Tk()
frame.config(background="palegoldenrod", padx=10, pady=10)

text_area = tk.Entry(
    frame,
    font=("times new roman", 20),  # font size for the user input
    foreground="navy",
    background="steelblue",
    show="*",  # used to replace each character with certain character (used for password textbox)
)
text_area.pack(side="left")


def handle_submit():
    global text_area
    print(text_area.get())
    # text_area.config(state="disabled")


submit_button = tk.Button(frame, text="Submit", command=handle_submit)
submit_button.pack(side="right")


def handle_delete():
    global text_area


text_area.delete(0, len(text_area.get()))  # .delete(starting_point,ending_point

delete_button = tk.Button(frame, text="delete", command=handle_delete)
delete_button.pack(side="right")


def handle_backspace():
    global text_area
    text_area.delete(len(text_area.get()) - 1, len(text_area.get()))


backspace_button = tk.Button(frame, text="backspace", command=handle_backspace)
backspace_button.pack(side="right")


frame.mainloop()
