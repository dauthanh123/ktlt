print('sinh vien:Đậu Đức Thành')
print('mssv:235752021610004')

def file_read_from_head(fname, nlines):
    from itertools import islice
    with open (fname) as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head(r'C:\zalo\ktddt\accc.txt',1)
