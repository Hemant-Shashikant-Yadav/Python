import tkinter as tk

window = tk.Tk()

frame = tk.Frame(window, background='black')
tk.Button(frame, text="W", font=("Consolas", 25), width=3).pack(side=tk.TOP)
tk.Button(frame, text="A", font=("Consolas", 25), width=3).pack(side=tk.LEFT)
tk.Button(frame, text="S", font=("Consolas", 25), width=3).pack(side=tk.LEFT)
tk.Button(frame, text="D", font=("Consolas", 25), width=3).pack(side=tk.LEFT)
frame.pack(side='top')
# frame.place(x=10,y=10)


window.mainloop()
