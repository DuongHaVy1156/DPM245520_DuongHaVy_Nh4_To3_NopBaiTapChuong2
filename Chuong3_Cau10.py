import math

# Nhập vào x và n
x = float(input("Nhập vào x: "))
n = int(input("Nhập vào n: "))

S = 0
for i in range(1, n+1):
    S += (x**i) / math.factorial(i)

print(f"Kết quả S({x}, {n}) = {S}")
