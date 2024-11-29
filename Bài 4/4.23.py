print("Sinh vien:Đậu Đức Thành")
print("Mssv:235752021610004")
sentence = input("Nhập câu: ")
letter_count = 0
digit_count = 0
for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
print(f"Số chữ cái là: {letter_count}")
print(f"Số chữ số là: {digit_count}")
