print('sinh vien:Đậu Đức Thành')
print('mssv:235752021610004')
import tkinter as tk

def nhan_nut():
    print("Bạn đã nhấn vào nút!")

window = tk.Tk()
window.title("Cửa sổ với nút bấm")

button = tk.Button(window, text="Nhấn vào đây", command=nhan_nut)
button.pack()

window.mainloop()
