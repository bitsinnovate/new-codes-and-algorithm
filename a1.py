n=int(input("enter a number (try 5 or 12 ):"))
print("binary number")
print("decimal",n,"-> binary",bin(n)[2:])
print("AND-both bits must be 1")

print("   12=",bin(12)[2:])
print("   10=",bin(10)[2:])
print("   12&10=",12&10)

print("OR-atleast one bit must be 1")
print("  12|10=", 12|10)