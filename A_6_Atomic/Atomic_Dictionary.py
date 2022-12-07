#Perform all operations inside a function
def AtomicDictionary():
    #create a dictionary
    atoms = {"H":"Hydrogen", "O":"Oxygen", "N" : "Nitrogen", "C" : "Carbon"}
    print(atoms)
    #add new elements 
    newSym = input("Enter atomic symbol: ")
    newEle = input("Enter atomic element name: ")
    atoms[newSym]=newEle
    print(f"Dictionary Updated : \n{atoms}")
    #number of atoms
    num = len(atoms.keys())
    print(f"Number of atomic elements in the dictionary are : {num}")
    #search 
    ser = input("Enter Atomic Element to search : ")
    if ser.title() in atoms.keys() or ser.title() in atoms.values():
        print(f"{ser} exists in the dictionary")
    else:
        print(f"{ser} does not exist in the dictionary")