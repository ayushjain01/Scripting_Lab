#Functions to Convert Temperature

def CtoK(degCel):
    return degCel + 273+15
def KtoC(kel):
    return kel - 273.15
def CtoF(degCel):
    return (degCel * 9/5) + 32
def FtoC(degFah):
    return (degFah - 32) * 5/9
def FtoK(degFah):
    return CtoK(FtoC(degFah))
def KtoF(kel):
    return CtoF(KtoC(kel))

#Store all conversions a in list of tuples
conversions = []
#Driver Code
ch = 1
while ch in range(1,8):
    print("""
Enter
1 - To convert from C to F
2 - To convert from F to C
3 - To convert from C to K
4 - To convert from F to K
5 - To convert from K to F
6 - To convert from K to C
7 - To view past conversions
""")
    ch = int(input(">>>"))
    if ch == 1:
        oldTemp = float(input("Enter Temperature in deg C : "))
        newTemp = CtoF(oldTemp)
        conversions.append((oldTemp,newTemp))
        print(f"{oldTemp} deg C = {newTemp} deg F")
    elif ch == 2:
        oldTemp = float(input("Enter Temperature in deg F : "))
        newTemp = FtoC(oldTemp)
        conversions.append((oldTemp,newTemp))
        print(f"{oldTemp} deg F = {newTemp} deg C")
    elif ch == 3:
        oldTemp = float(input("Enter Temperature in deg C : "))
        newTemp = CtoK(oldTemp)
        conversions.append((oldTemp,newTemp))
        print(f"{oldTemp} deg C = {newTemp} K")
    elif ch == 4:
        oldTemp = float(input("Enter Temperature in deg F : "))
        newTemp = FtoK(oldTemp)
        conversions.append((oldTemp,newTemp))
        print(f"{oldTemp} deg F = {newTemp} K")
    elif ch == 5:
        oldTemp = float(input("Enter Temperature in K : "))
        newTemp = KtoF(oldTemp)
        conversions.append((oldTemp,newTemp))
        print(f"{oldTemp} K = {newTemp} F")
    elif ch == 6:
        oldTemp = float(input("Enter Temperature in K : "))
        newTemp = KtoC(oldTemp)
        conversions.append((oldTemp,newTemp))
        print(f"{oldTemp} K = {newTemp} C")
    elif ch == 7:
        print(
            """
            Enter
            1 - To Sort according to From Value
            2 - To Sort according to To value
            """)
        ch1 = int(input(">>>"))
        if ch1 == 1:
            print("Past Conversions : ")
            for (i,j) in conversions:
                print(f"{i} --> {j}")
        elif ch1 == 2:
            print("Past Conversions : ")
            for (i,j) in conversions:
                print(f"{j} --> {i}")
        else:
            print("Invalid")
    else:
        print("Invalid Option! Please Try Again")
