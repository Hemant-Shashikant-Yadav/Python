import tkinter as tk

frame = tk.Tk()
frame.geometry('600x600')


new_menubar = tk.Menu(master=frame)
new_menubar.config(background='red')

menu1 = tk.Menu(new_menubar, tearoff=0)
menu1.add_command(label='1', command=lambda: print('1'))
menu1.add_command(label='2', command=lambda: print('2'))
menu1.add_separator()
menu1.add_command(label='3', command=lambda: print('3'))

menu2 = tk.Menu(new_menubar, tearoff=0)
menu2.add_command(label='hi')
menu2.add_command(label='hello')
menu2.add_command(label='hey')


# adding menu to menubar
new_menubar.add_cascade(label="menuitem 1", menu=menu1)
new_menubar.add_cascade(label='something', menu=menu2)
# adding menubar to frame
frame.config(menu=new_menubar)

frame.mainloop()
