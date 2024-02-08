import tkinter as tk


frame = tk.Tk()
image = tk.PhotoImage(file="image.png")
# checkbutton_boolean_variable = tk.BooleanVar()
checkbutton_string_variable = tk.StringVar(value="the checkbox is not active")
new_checkbutton = tk.Checkbutton(
    frame,
    text="this is checkbutton",
    font=("comic sans ms", 20, "bold"),
    variable=checkbutton_string_variable,
    onvalue="the checkbox is clicked",  # sets the value to `variable` when the checkbox is checked
    offvalue="this is most random shit ever",  # sets the value to `variable` when the checkbox is unchecked after checking is done
    # variable=checkbox_boolean_variable,
    # onvalue=True,
    # offvalue=False,
    command=lambda: print(f"Checkbox is updated"),
    foreground="red",
    background="aqua",
    activeforeground="red",  # when the checkbox is in active state
    activebackground="aqua",  # when the checkbox is in active state
    image=image,
    compound="bottom",
)

new_checkbutton.pack()

new_button = tk.Button(
    frame, text="submit", command=lambda: print(checkbutton_string_variable.get())
)
new_button.pack()


frame.mainloop()
