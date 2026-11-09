print("XOR swap - exchange two values without a third variable")
print(" before:a=5 b=9")
a,b=5,9
a^=b; b^=a; a^=b
print(" after:a=",a, " b=",b)
n=int(input("enter a number(try 3 or 7):"))
a,b=n,8
a^=b; b^=a; a^=b
print("XOR swap exchanges the values")
print(" n became:",a)