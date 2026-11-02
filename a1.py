print("XOR with 0 keeps the number")
print("  5^0=", 5^0)
print("  9^0=", 9^0)

print("XOR with itself givess 0")
print("  5^5=", 5^5)
print("  9^9=", 9^9)

n=int(input("enter a number(try 6 or 11):"))
guess = input(" what is 3^"+ str(n)+" ^3?")
print("XOR cances - 3 appears twice so it dissapears")
print(" 3^",n,"^3=",3^n^3,"  your guess:",guess)