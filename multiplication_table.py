print("*** Multiplication table ***\n")
a = int(input("Enter the number you want to multiplication table for : "))
for i in range (1,11):
    b = a * i
    print(f"{a} * {i} = ", b)
