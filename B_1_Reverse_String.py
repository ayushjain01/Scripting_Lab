"""Write a python class to reverse a sentence (initialized via constructor) word by word. 
Example: “I am here” should be reversed as “here am I”. Create instances of this class 
for each of the three strings input by the user and display the reversed string for each, in descending order of number of vowels in the string."""

#reverse word by word : "hear am i" becomes "i am here"
class revStr():
    def __init__(self,sen):
        self.sen = sen
    def rev(self):      #reverse word by word
        x = self.sen.split(" ")
        x.reverse()
        s = " ".join(x)
        return s
    def countVow(self): #count number of vowels
        c = 0
        self.sen.lower()
        for i in self.sen:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                c+=1
        return c
#initialize three objects
str1 = revStr("My name is ayush")
str2 = revStr("I want to go home")
str3 = revStr("I am funny")

strList = [(str1.rev(),str1.countVow()), (str2.rev(),str2.countVow()), (str3.rev(),str3.countVow())]
strList.sort(key = lambda x: x[1])  #sort in desc order of number of vowels
strList.reverse()
for i in strList:   #print in desc order of number of vowels
    print(f"{i[0]}")