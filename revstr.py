class revStr():
    def __init__(self,sen):
        self.sen = sen
    def rev(self):
        x = self.sen.split(" ")
        x.reverse()
        s = " ".join(x)
        return s
    def countVow(self):
        c = 0
        self.sen.lower()
        for i in self.sen:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                c+=1
        return c

str1 = revStr("My name is ayush")
str2 = revStr("I want to go home")
str3 = revStr("I am funny")
strList = [(str1.rev(),str1.countVow()), (str2.rev(),str2.countVow()), (str3.rev(),str3.countVow())]
strList.sort(key = lambda x: x[1])
strList.reverse()
for i in strList:
    print(f"{i[0]}")