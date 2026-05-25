numbs = []
for i in range (10):
    numb = int(input(f"Enter the {i+1} number you want to check : "))
    numbs.append(numb)
print("The numbers you wrote are", numbs)
z = []
eve = []
oddo = []
for i in numbs:
    if i  == 0:
        z.append(i)
    elif i % 2 == 0:
        eve.append(i)
    else :
        oddo.append(i)
if (len(oddo)) != 0 :
    print(f"The number of odd numbers from the list are {len(oddo)} and as follows : ",oddo)
if (len(eve)) != 0 :
    print(f"The number of even numbers from the list are {len(eve)} and as follows : ", eve)
if (len(z)) != 0 :
    print(f"The number of 0's  from the list are {len(z)})
