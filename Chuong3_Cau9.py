# Nhập tháng từ người dùng
thang = int(input("Nhập vào số tháng (1-12): "))

# Kiểm tra tháng thuộc quý mấy
if 1 <= thang <= 3:
    quy = 1
elif 4 <= thang <= 6:
    quy = 2
elif 7 <= thang <= 9:
    quy = 3
elif 10 <= thang <= 12:
    quy = 4
else:
    quy = None

# In kết quả
if quy:
    print(f"Tháng {thang} thuộc quý {quy} trong năm.")
else:
    print("Tháng không hợp lệ. Vui lòng nhập số từ 1 đến 12.")
