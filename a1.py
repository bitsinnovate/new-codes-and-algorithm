print("n & ( n - 1) clears the rrightmost set bit")
print(" 12&11=",12&11, " binary:",bin(12&11)[2:])
print(" 8&7=",8&7)
n=int(input("enter a number(try 4 or 6):"))
print(" power of 2 :n&(n-1)==0 means only one bit is one")
if n>0 and(n&(n-1))==0:
    print(" ",n," binary:",bin(n)[2:])
else:
    print(" ",n," binary:",bin(n)[2:])