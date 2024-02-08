import tkinter as tk

# The `messagebox` module in Tkinter is a sub-module inside the main Tkinter library, so above line will import all the files and below line will import messagebox directory's files
from tkinter import messagebox


def show_message_box():
    # messagebox.showinfo(title="simple info box", message="you clicked the button")

    # messagebox.showerror(title="error box", message="you clicked the button")

    # it makes different sound during popup and I like it
    messagebox.showwarning(title="Warning box", message="you clicked the button")


def user_input_message_box():
    # ok_cancel_bool_value = messagebox.askokcancel(
    #     title="????", message="are you sure about that"
    # )
    # if ok_cancel_bool_value:
    #     messagebox.showinfo("title", "you clicked on okay")
    # else:
    #     messagebox.showinfo("title", "you clicked on cancel")

    # retry_cancel_bool_value = messagebox.askretrycancel(
    #     title="!!!!", message="failed to do nothing"
    # )
    # if retry_cancel_bool_value:
    #     messagebox.showinfo(title="title", message="you clicked retry")
    # else:
    #     messagebox.showinfo(title="title", message="you clicked cancel")

    # ask_yes_no_bool_value = messagebox.askyesno(
    #     title="title", message="message"
    # )
    # if ask_yes_no_bool_value:
    #     messagebox.showinfo(message="you clicked yes")
    # else:
    #     messagebox.showinfo(message="you clicked no")

    # ask_question_string_value = messagebox.askquestion(
    #     title="question", message="how are you??"
    # )
    # if ask_question_string_value == "yes":
    #     messagebox.showinfo(message="nice!!!")
    # elif ask_question_string_value == "no":
    #     messagebox.showinfo(message="what happened??")

    ask_yes_no_cancel_value = messagebox.askyesnocancel(
        title="huh??", message="do you want to continue??"
    )

    if ask_yes_no_cancel_value == True:
        messagebox.showinfo(message="you clicked yes")
    elif ask_yes_no_cancel_value == False:
        messagebox.showinfo(message="you clicked no")
    elif ask_yes_no_cancel_value == None:
        messagebox.showinfo(message="you clicked cancel or closed the message window")


frame = tk.Tk()

frame.config(padx=10, pady=10)

button = tk.Button(
    master=frame,
    text="click me",
    font=("arial", 30),
    bg="brown",
    fg="lightblue",
    activebackground="brown",
    activeforeground="blue",
    command=user_input_message_box,
)
button.pack()


frame.mainloop()
