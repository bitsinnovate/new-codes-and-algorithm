n = 10
guess = input("Double Loop at n = 10 checks n x n pairs. how many?")

input("Formula:one calculation,done.Press enter to run")
steps = 1
print(" steps=",steps," -> 0(1) constant time -> steps never change")

input("loop:one step per item.Press enter to run")
steps=0
for i in range(n):
    steps +=1
print(" steps=",steps," -> 0(n) linear time -> steps grow with n")   

input("double loop:checks every pair .Press enter to run")
steps=0
for i in range(n):
    for j in range(n):
     steps +=1
print(" steps=",steps," your guess:",guess," -> o(n^2) quadriatic time")   

input("two more notifications.press enter")
print(" big omega -> best lower case bound")
print(" big theta 0 -> exact bound(worst = best)")