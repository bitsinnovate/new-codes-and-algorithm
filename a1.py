print("set a bit-OR turns it ON")
print("  5=",bin(5)[2:])
print("  5|2=",5|2," binary:",bin(5|2)[2:])

print("zero a bit-AND turns it OF")
print("  7=",bin(7)[2:])
print("  7&5=",7&5," binary:",bin(7&5)[2:])

n=int(input("enter a number(try 4 or 6):"))

print("power of 2 - only 1 bit is ON")
if n>0 and(n&(n-1))==0:
  print(" ",n,"  binary:", bin(n)[2:])
else:
  print(" ",n,"  binary:", bin(n)[2:])