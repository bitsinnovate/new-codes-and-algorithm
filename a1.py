from math import sqrt
n = int(input("Enter a 2-digit number: "))
if not (10 <= n <= 99):
    print("Error: The number must be a 2-digit number (10 to 99).")
if (n>1):
    for i in range(2,int(sqrt(n)+1)):
        if n%i == 0:
            print(n, "is not prime number")
            break
    else:
        print(n, "is prime")

else:
    print(n, "is not prime")
