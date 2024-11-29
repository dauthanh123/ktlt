print('sinh vien:Đậu Đức Thành')
print('mssv:235752021610004')
class Chuoi:
    def __init__(self):
        self.string = ""

    def get_String(self):
       
        self.string = input("Nhập chuỗi: ")

    def print_String(self):
       
        print("Chuỗi in hoa:", self.string.upper())
        
chuoi = Chuoi()

chuoi.get_String()

chuoi.print_String()

