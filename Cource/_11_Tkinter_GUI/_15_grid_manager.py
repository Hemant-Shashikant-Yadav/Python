import tkinter as tk

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


submit_button = tk.Button(
    master=window,
    text='submit the form',
    font=('arial', 15),
    command=window.destroy
)
# columnspan indicates that this component will take up defined colums
submit_button.grid(row=4, column=0, columnspan=2)

window.mainloop()
