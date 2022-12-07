from functools import reduce

#create list of 6 numbers
numList = [10,20,30,40,50,60]
#use list comprehension and make a new list
newList = [i*3 for i in numList]
#sum of list elements
sum = reduce(lambda a, b: a+b, numList)
print(f"Sum of elements in {numList} is {sum}")
sum = reduce(lambda a, b: a+b, newList)
print(f"Sum of elements in {newList} is {sum}")