decimal = 1996

rules = { 1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I" }


def decToRom(decimal: int) -> None:
    print(decimal, "=", end=" ")
    while decimal != 0:
        for rule in rules:
            if decimal - rule >= 0:
                decimal -= rule
                print(rules[rule], end="")
                if decimal >= rule:
                    break


decToRom(decimal)
