print('sinh vien:Đậu Đức Thành')
print('mssv:235752021610004')
import tkinter as tk

def show_radio_choice():
    selected_value = radio_var.get()
    label_choice.config(text=f"Số bạn chọn: {selected_value}")
root = tk.Tk()
root.title("Radio Button Example")
root.geometry("300x200")
radio_var = tk.IntVar()
radio_button1 = tk.Radiobutton(root, text="First", variable=radio_var, value=1)
radio_button1.pack()

radio_button2 = tk.Radiobutton(root, text="second", variable=radio_var, value=2)
radio_button2.pack()

radio_button3 = tk.Radiobutton(root, text="Third", variable=radio_var, value=3)
radio_button3.pack()

button_click = tk.Button(root, text="Click Me", command=show_radio_choice)
button_click.pack()
label_choice = tk.Label(root, text="")
label_choice.pack()
root.mainloop()
