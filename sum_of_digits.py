num = int(input("Enter number : "))
total = 0
while num > 0:
    digit = num % 10
    total = digit + total
    num = num // 10
print(f"Sum of the numbers are : {total}")

