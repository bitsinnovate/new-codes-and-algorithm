scores = [3,7,2,9,4,1,8,5,6]

input("list:"+str (scores)+"  n=9 linear search - checks left to write.press enter")
target = int(input("enter a number to search for:"))
input("searching for "+ str(target)+ ".press enter to run")
steps = 0
for score in scores:
    steps +=1
    if score == target:
        break
print(" target=",target," found at position",steps," checks=",steps)   
input("compare with worst and best case.press enter")
mid = len(scores)//2
print(" best:1check -> 0(1) average:",mid, "checks -> 0(n)  worst: 9 checks -> 0(n) yours:", steps)
input("all three cases . press enter")
print(" best 0(1) average 0(n) worst 0(n)  ->  big-0 = worst case = 0(n).")