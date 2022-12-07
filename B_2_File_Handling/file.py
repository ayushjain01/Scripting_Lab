from functools import reduce
import os
import sys
#read contents of a file and store number of occurrences of each word in a dictionary
myfile = open(os.path.join(sys.path[0], "myfile.txt"),"r") #read mode
occurrences = {}
content = myfile.read()
content = content.split(" ")
#count number of occurrences
for word in content:
    if word in occurrences.keys():
        occurrences[word] = occurrences[word] + 1
    else:
        occurrences[word] = 1
#top 10 words
top10 = list(occurrences.items())
#print(top10)
top10.sort(key = lambda x: x[1])  #sort in desc order of number of occurrences
top10.reverse()
top10 = top10[0:10] #top 10 words
length = []
print("Top 10 words from the text are :")
print("Word\t Occurrences")
for i in top10:
    print(f"{i[0]}\t\t{i[1]}")
    length.append(len(i[0])) #store length of each word
print(f"Length List : {length}")

average = reduce(lambda a, b: a + b, length) / len(length)   #calculate average
odd = [x*x for x in length if x%2 == 1]          #calculate square of odd numbers
print(f"Average Length: : {average}")
print(f"Odd Square List : {odd}")
myfile.close()