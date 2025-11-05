# Đề bài
# if i < j:
#     if j < k:
#         i = j
#     else:
#         j = k
# else:
#     if j > k:
#         j = i
#     else:
#         i = k
# print("i =", i, ", j =", j, ", k =", k)

# Các trường hợp:
cases = [
    (3, 5, 7),
    (3, 7, 5),
    (5, 3, 7),
    (5, 7, 3),
    (7, 3, 5),
    (7, 5, 3)
]

for i, j, k in cases:
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print(f"Trường hợp (i={i}, j={j}, k={k}) → Kết quả: i={i}, j={j}, k={k}")
