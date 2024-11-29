print('sinh vien:Đậu Đức Thành')
print('mssv:235752021610004')
import tkinter as tk

def show_info():
    name = entry_name.get()
    dob = entry_dob.get()
    mssv = entry_mssv.get()
    major = entry_major.get()
    
    label_info.config(text=f"Họ tên: {name}\nNgày sinh: {dob}\nMSSV: {mssv}\nNgành học: {major}")
root = tk.Tk()
root.title("Thông tin cá nhân")
root.geometry("300x250")
tk.Label(root, text="Họ tên:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Ngày sinh (dd/mm/yyyy):").pack()
entry_dob = tk.Entry(root)
entry_dob.pack()

tk.Label(root, text="MSSV:").pack()
entry_mssv = tk.Entry(root)
entry_mssv.pack()

tk.Label(root, text="Ngành học:").pack()
entry_major = tk.Entry(root)
entry_major.pack()
button_show = tk.Button(root, text="Hiển thị thông tin", command=show_info)
button_show.pack()
label_info = tk.Label(root, text="", justify="left")
label_info.pack()
root.mainloop()
