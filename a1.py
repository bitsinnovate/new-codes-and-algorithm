scores = [1,3,5,7,9,11,13,15,17]
input ("list: " + str(scores) + " n=9 press enter")
guess = input("max checks to find any number from this list?")
target = int(input("pick a number from the list:"))

input ("binary search - checks the middle, drops half each round press enter")
low,high = 0,len(scores) - 1
steps = 0
while low <= high:
    mid = (low+high) //2
    steps +=1
    print(" round",steps," -> checked", scores[mid])
    if scores[mid] == target:
       break
    elif scores[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
    print(" found",target," at positionn",mid+1, "in" , steps," steps your guess:",guess ," -> O(log n)")
    input("steps grow slowly with n press enter")
    for n,s in[(9,4),(100,7),(1000,10)]:
        print(" n =",n," max steps =",s," ->O(log n)")