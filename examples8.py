# Find the largest number
numbers = [5,9,2,10,3,7]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
else:
    print ("the largest number is:", largest)
