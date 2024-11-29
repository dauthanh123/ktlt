print("Sinh vien:Đậu Đức Thành")
print("Mssv:235752021610004")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
P = tuple(i for i in range(1_000_000) if is_prime(i))
print("Tuple P gồm các số nguyên tố nhỏ hơn 1 triệu:")
print(P[:20])
