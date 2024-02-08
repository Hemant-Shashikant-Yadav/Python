# Tabs are something like routing that we use in React

import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

new_notebook = ttk.Notebook(master=window)

frame1 = tk.Frame(new_notebook)
tk.Label(frame1, text='this is tab 1', font=(
    'monospace', 35), fg='violet').pack()

frame2 = tk.Frame(new_notebook)
tk.Label(frame2, text='you guessed right this is tab 2', font=(
    'monospace', 35), fg='orange').pack(expand=True)  # using expand to keep the added component in the center even when the parent element changes it's size

new_notebook.add(frame1, text='tab1')
new_notebook.add(frame2, text='tab2')

# expand --> expand with parent,both --> both x and y axis
new_notebook.pack(expand=True, fill='both')

window.mainloop()
