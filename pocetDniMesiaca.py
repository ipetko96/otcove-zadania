import calendar

while True:
    year = input("zadaj rok: ")
    if year.isdigit():
        break
    else:
        print("nezadal si cislovku")

while True:
    month = input("zadaj mesiac: ")
    if month.isdigit() and 1 <= int(month) <= 12:
        break
    else:
        print("nezadal si cislovku")

dayCount = calendar.monthrange(int(year), int(month))[1]
print(f"mesiac {month} v roku {year} ma {dayCount} dni")
