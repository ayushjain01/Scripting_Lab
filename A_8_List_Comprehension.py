"""Create a list of 6 numbers. Use ‘list-comprehension’ to create a new list where each element in the original list is multiplied by 3. 
Use ‘lambda’ and ‘reduce’ function find the sum of the elements of the original list as well as the new list."""

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