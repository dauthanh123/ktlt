print("Sinh vien:Đậu Đức Thành")
print("Mssv:235752021610004")
n = int(input("Nhập số n: "))

for i in range(1, n):
  total = sum(j for j in range(1, i) if i % j == 0)
  if total > i:
        print(i)

