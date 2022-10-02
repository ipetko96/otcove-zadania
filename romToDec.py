### Prevod rimskeho cisla na decimalne ###
x = "MCLXV"
# y1 = [str(numeric_string) for numeric_string in x]
znaky = ["M", "D", "C", "L", "X", "V", "I"]
for i in x:
    if i not in znaky:
        print("Nespravne znaky v rimskom cisle. Pouzi iba pismena: M, D, C, L, X, V, I")
        break
if x.count("I") > 3:
    print("Nespravne rimske cislo.")
if x.count("X") > 3:
    print("Nespravne rimske cislo.")
if x.count("C") > 3:
    print("Nespravne rimske cislo.")
d11 = 0
d12 = 0
d13 = 0
d14 = 0
d15 = 0
d16 = 0
if "CD" in x:
    d11 = d11 + 400
    x = x.replace("CD", "")
if "IV" in x:
    d12 = int(4) + d12
    x = x.replace("IV", "")
if "XL" in x:
    d13 = int(40) + d13
    x = x.replace("XL", "")
if "IX" in x:
    d14 = int(9) + d14
    x = x.replace("IX", "")
if "XC" in x:
    d15 = int(90) + d15
    x = x.replace("XC", "")
if "CM" in x:
    d16 = int(900) + d16
    x = x.replace("CM", "")

d17 = (x.count("M")) * 1000
d18 = (x.count("D")) * 500
d19 = (x.count("C")) * 100
d20 = (x.count("L")) * 50
d21 = (x.count("X")) * 10
d22 = (x.count("V")) * 5
d23 = x.count("I")
# print(x)
d = d11 + d12 + d13 + d14 + d15 + d16 + d17 + d18 + d19 + d20 + d21 + d22 + d23
print(d)
