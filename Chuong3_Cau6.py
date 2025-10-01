def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", 
                 "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 0 or n > 99:
        return "Số không hợp lệ. Vui lòng nhập số từ 0 đến 99."
    
    if n < 10:
        if n == 5:
            return "năm"
        else:
            return don_vi[n]
    else:
        chuc = n // 10
        donvi = n % 10

        if donvi == 0:
            return hang_chuc[chuc]
        elif donvi == 1 and chuc > 1:
            return hang_chuc[chuc] + " mốt"
        elif donvi == 5 and chuc >= 1:
            return hang_chuc[chuc] + " lăm"
        else:
            return hang_chuc[chuc] + " " + don_vi[donvi]

# Nhập số từ người dùng
n = int(input("Nhập số nguyên n (0-99): "))
print("Cách đọc:", doc_so(n))
