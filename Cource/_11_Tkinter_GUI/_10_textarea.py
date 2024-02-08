import tkinter as tk


def handle_submit_button_click():
    # yeah it's weird but textarea work like this only in Tkinter
    print(textarea.get("1.00", tk.END))


frame = tk.Tk()

textarea = tk.Text(
    frame,
    bg="palegoldenrod",
    font=("segoe print", 40),
    height=4,  # how much rows of character should visible 
    width=10,  # how much colums of character should visible
    fg="red",
)
textarea.pack()
submit_button = tk.Button(text="submit", command=handle_submit_button_click)
submit_button.pack()

frame.mainloop()
