## Prevod decimalneho cisla na rimske ###
x = 1996
r1 = x // 1000
rim1 = r1 * "M"
r2 = x - r1 * 1000
r3 = r2 // 100
rim2 = r3 * "C"
if r3 == 5:
    rim2 = "D"
elif r3 == 9:
    rim2 = "CM"
elif r3 == 4:
    rim2 = "CD"
elif r3 == 4:
    rim2 = "CD"
elif r3 == 6:
    rim2 = "DC"
elif r3 == 7:
    rim2 = "DCC"
elif r3 == 8:
    rim2 = "DCCC"
r4 = r2 - r3 * 100
r5 = r4 // 10
rim3 = r5 * "X"
if r5 == 9:
    rim3 = "XC"
elif r5 == 5:
    rim3 = "L"
elif r5 == 4:
    rim3 = "XL"
elif r5 == 5:
    rim3 = "L"
elif r5 == 6:
    rim3 = "LX"
elif r5 == 7:
    rim3 = "LXX"
elif r5 == 8:
    rim3 = "LXXX"
r6 = r4 - r5 * 10
rim4 = r6 * "I"
if r6 == 4:
    rim4 = "IV"
elif r6 == 5:
    rim4 = "V"
elif r6 == 6:
    rim4 = "VI"
elif r6 == 7:
    rim4 = "VII"
elif r6 == 8:
    rim4 = "VIII"
elif r6 == 9:
    rim4 = "IX"
rim_x = rim1 + rim2 + rim3 + rim4
print(rim_x)
