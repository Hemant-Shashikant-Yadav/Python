import tkinter as tk

food_list = ["modak", "shahi-paneer", "chinch", "puranpoli"]


def handle_radio_button_click():
    for item in food_list:
        if item == radio_button_group_variable.get():
            print(f"you wanna order {item}??")


frame = tk.Tk()

radio_button_group_variable = tk.StringVar(
    value="modak"
)  # making the default value 0 so that the radiobutton with value 0 will get selected automatically

for item in food_list:
    radio_button = tk.Radiobutton(
        frame,
        text=item,
        variable=radio_button_group_variable,  # whichever radiobutton will have the same value as variable, it will be selected
        value=item,  # giving value will differentiate them from each other, radiobuttons having same values will be triggered all at once even on of them is triggered on or off due to having same `variable` as `radio_button_group_variable`
        font=("young serif", 25),
        command=handle_radio_button_click,
    )
    radio_button.pack(anchor="w")


frame.mainloop()
