import tkinter as tk


def create_new_window():
    new_window = tk.Tk()

    tk.Button(new_window, text="delete this window",
              command=new_window.destroy).pack()

    tk.Button(new_window, text='create new window like this',
              command=create_new_window).pack()

    tk.Button(new_window, text='create new window having parent as this window',
              command=lambda: tk.Toplevel(master=new_window)).pack()

    new_window.config(padx=10, pady=10)
    new_window.mainloop()
    

 


create_new_window()
