a = int(input("enter number1:"))
b = int(input("enter number2:"))

greater = max(a,b)
smallest = min(a,b)
for i in range(greater,a*b+1,greater):
    if i % smallest == 0:
        break
print(i)