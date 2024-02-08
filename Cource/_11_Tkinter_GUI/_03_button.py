# another way to import the module
import tkinter as tk

# using tk.method_name() will avoid the name ambiguity in the program if there are multiple methods with same name
# and we can specify that we want to call the method from `tkinter` module itself

a = 1


def handle_button_click():
    # accessing the global variable `a`, cause even functions are class in the background of python, {yeah python gets weird sometimes cause if we are only reading the value that's okay but when we try to assign the value it creates it's own local variable so instead of updating value it initialize the variable and perform assingment operation, that's why I think having a keyword indicating the initialization operation is being performed is good in a programming language like JavaScript(best language BTW)}
    global a
    print(f"button clicked {a}")
    a = a + 1


frame = tk.Tk()
frame.config(padx=10, pady=10, background="powderblue")

photo_for_button = tk.PhotoImage(file="image.png")


new_button = tk.Button(frame)
new_button.pack()
new_button.config(
    text="click me",
    command=handle_button_click,  # This is same as adding a ActionListener
    # here we didn't call the method by using paranthesis we just simply made the command function same as handle_button_click function cause if we did something like `command = handle_button_click()` then we would have assinged the return value fo handle_button_click to the command function
    # this phenomenon is known as `callback`
    font=("comic sans MS", 30, "underline"),
    background="steelblue",
    activebackground="darkblue",  # background color when button is clicked
    activeforeground="darkgray",  # font color when button is clicked
    # state="disabled", # same as setEnabled in swing
    image=photo_for_button,
    compound="top",
)


frame.mainloop()
