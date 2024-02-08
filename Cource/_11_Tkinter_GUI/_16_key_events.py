import tkinter as tk


# the bind method will pass the event object to recieved function for callback
# the event object contains information about key pressed with position of the element that caused the event to fire up

def handle_form_submission(event):
    print("form submitted")


window = tk.Tk()

window.config(padx=10, pady=10)


first_name_label = tk.Label(master=window, text='Enter Your First Name')
first_name_entry = tk.Entry(master=window)

first_name_label.grid(row=1, column=0)
first_name_entry.grid(row=1, column=1)

last_name_label = tk.Label(master=window, text='Enter Your Last Name')
last_name_entry = tk.Entry(master=window)

last_name_label.grid(row=2, column=0)
last_name_entry.grid(row=2, column=1)

email_label = tk.Label(master=window, text='Enter Your E-mail')
email_entry = tk.Entry(master=window)
email_label.grid(row=3, column=0)
email_entry.grid(row=3, column=1)
# adding the return(enter) button press to call the function
email_entry.bind('<Return>', handle_form_submission)

submit_button = tk.Button(
    master=window,
    text='submit the form',
    font=('arial', 15),
    command=lambda: handle_form_submission(None)
)
submit_button.bind('<Return>', handle_form_submission)
submit_button.grid(row=4, column=0, columnspan=2)

window.mainloop()
