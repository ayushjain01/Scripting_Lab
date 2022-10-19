from functools import reduce

numList = [10,20,30,40,50,60]
newList = [i*3 for i in numList]
sum = reduce(lambda a, b: a+b, numList)
print(f"Sum of elements in {numList} is {sum}")
sum = reduce(lambda a, b: a+b, newList)
print(f"Sum of elements in {newList} is {sum}")