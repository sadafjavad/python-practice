# count how many times 3 appears
numbers = [3,5,6,8,3,3,3,3,3,6,9,6,]
count = 0
for num in numbers:
    if num == 3:
        count +=1
else:
    print ("3 appears",count, "times.")
