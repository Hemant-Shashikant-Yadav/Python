import tkinter as tk


def handle_submit_button_click():
    print(new_listbox.get(new_listbox.curselection()))


def handle_add_button_click():
    new_listbox.insert(new_listbox.size(), textarea.get())
    new_listbox.config(height=new_listbox.size())


def handle_delete_button_click():
    new_listbox.delete(new_listbox.curselection())
    new_listbox.config(height=new_listbox.size())


frame = tk.Tk()
frame.config(padx=10, pady=10, background="navy")
new_listbox = tk.Listbox(frame, font=("constantia", 30))

for i in range(5):
    new_listbox.insert(i, "list item: " + str(i + 1))

new_listbox.configure(height=new_listbox.size(), background="steelblue")
new_listbox.pack()

textarea = tk.Entry(frame)
textarea.pack()

add_button = tk.Button(frame, text="add", command=handle_add_button_click)
add_button.pack()

delete_button = tk.Button(frame, text="delete", command=handle_delete_button_click)
delete_button.pack()


submit_button = tk.Button(frame, text="submit", command=handle_submit_button_click)
submit_button.pack()

frame.mainloop()
