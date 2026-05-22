a=[]
for i in range(10):
    mark = float(input(f"Enter the mark of Student {i+1} : "))
    a.append(mark)
print("Marks list : ", a)
print("\n")
maxi = max(a)
mini = min(a)
print("The Highest marks achieved is : ", maxi)
print("\n")
print("The Least marks achieved is : ", mini)
print("\n")
b=[]
c=[]
for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])
    else :
        c.append(a[i])
print(f"Total Even number(s) in the marks list are {len(b)} and as follows : ", b)
print(f"Total Odd number(s) in the marks list are {len(c)} and as follows : ", c)
        
