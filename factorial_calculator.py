i = int(input("Enter a number : "))
fact = 1
num = i
while i > 1 : 
    fact = i * fact
    i = i - 1
print(f"Factorial of {num} is : ", fact)
