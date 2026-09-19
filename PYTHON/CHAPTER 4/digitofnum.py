n = int(input("Enter a number: "))

n = abs(n)

if n == 0:
    print(0)
else:
    while n > 0:
        digit = n % 10
        print(digit)
        n = n // 10
