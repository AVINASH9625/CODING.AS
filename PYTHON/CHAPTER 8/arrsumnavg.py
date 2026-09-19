n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

total = sum(arr)
average = total / n

print("Sum =", total)
print("Average =", average)
