import re

roman = "MCMXCVI"
decimal = 0

rules = { "M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1 }
regexPattern = r"^M*D{0,1}(CM){0,1}?C{0,3}(CD){0,1}?L{0,1}(XC){0,1}?X{0,3}(XL){0,1}?V{0,1}(IX){0,1}?I{0,3}(IV){0,1}?$"

print(roman, "=", end=" ")
if not re.match(regexPattern, roman):
    print("Non valid roman number.")
else:
    while len(roman) != 0:
        for rule in rules:
            if roman[:2] == rule:
                roman = roman[2:]
                decimal += rules[rule]
                break
            if roman[:1] == rule:
                roman = roman[1:]
                decimal += rules[rule]
                break
    print(decimal)
