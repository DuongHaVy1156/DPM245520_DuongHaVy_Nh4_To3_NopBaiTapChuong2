def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
def days_in_month(month, year):
    if month in (1,3,5,7,8,10,12):
        return 31
    if month in (4,6,9,11):
        return 30
    return 29 if is_leap(year) else 28
def next_day(d, m, y):
    if not (1 <= m <= 12):
        raise ValueError("Tháng không hợp lệ")
    dim = days_in_month(m, y)
    if not (1 <= d <= dim):
        raise ValueError("Ngày không hợp lệ cho tháng/năm trước")
    d += 1
    if d > dim:
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1
    return d, m, y

if __name__ == "__main__":
    s = input("Nhập ngày theo dd/mm/yyyy: ").strip()
    d, m, y = map(int, s.split("/"))
    nd, nm, ny = next_day(d, m, y)
    print (f"Ngày kế tiếp: {nd:02d}/{nm:02d}/{ny}") 