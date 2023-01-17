""" Write Python code to do the following operations:
    - Create a dictionary that contains the atomic element symbol and its name.
    - Add a unique & duplicate element into this dictionary by interacting with the user. Observe the output and justify it.
    - Display the number of atomic elements in this dictionary.
    - Ask user to enter an element to search in the dictionary. Display appropriate results.
    Rewrite this program so that these operations are inside a function called ‘AtomicDictionary’. 
    Create another python file called “Atomic.py” and execute this function in it."""

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