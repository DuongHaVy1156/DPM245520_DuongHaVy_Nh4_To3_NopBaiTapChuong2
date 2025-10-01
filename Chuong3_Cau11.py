def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    n = int(input("Nhập vào một số nguyên: "))
    
    if is_prime(n):
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
    
    tiep_tuc = input("Bạn có muốn tiếp tục? (c/k): ").lower()
    if tiep_tuc != 'c':
        print("Thoát chương trình.")
        break
