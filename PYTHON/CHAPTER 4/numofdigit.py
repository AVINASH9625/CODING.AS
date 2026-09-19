n = int(input("Enter a number: "))

n = abs(n)

if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        n = n // 10
        count += 1

print("Number of digits =", count)
