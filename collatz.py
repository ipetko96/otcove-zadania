def collatz(n: int) -> int:
    while n > 1:
        if n % 2:
            return 3 * n + 1
        else:
            return n // 2


x = 674

for _ in range(7):
    x = collatz(x)

print(x)
