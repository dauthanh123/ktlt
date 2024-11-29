print('sinh vien:Đậu Đức Thành')
print('mssv:235752021610004')
input_file=open(r"C:\zalo\ktddt\accc.txt",'r')
for line in input_file:
    l=len(line)
    s=' '
    while(l>=1):
        s=s+line[l-1]
        l=l-1
    print(s)
input_file.close()
