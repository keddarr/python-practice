print("***Prime number checker***")
num = int(input("Enter a number : "))
if num <= 1 :
    print("Not a Prime number")
else:
    prime = True
    for i in range(2,num):
        if num % i == 0 :
            prime = False
            break
    if prime :
        print( "Is a prime number")
    else : 
        print("Not a Prime number")
