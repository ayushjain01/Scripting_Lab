"""Write Python code to do the following:
      - Create list with inputs from user
      - Determine minimum and maximum elements in the list
      - Insert new element into the list
      - Delete an element from the list
      - Determine if an element is present in the list."""

#Create a List with inputs from user
a = list(map(int, input("Enter elements separated by space : ").split(" "))) 
#Determine min and max 
min_a = min(a)
max_a = max(a)
print(f"Minimum Element in list - {min_a}")
print(f"Maximum Element in list - {max_a}")
#Insert new element
new = int(input("Enter new element: "))
a.append(new)
print(f"Element Added : {a}")
#Delete an element
rem = int(input("Enter an element to delete: "))
a.remove(new) 
print(f"Element Deleted : {a}")
#Search an element
ser = int(input("Enter an element to search: "))
if ser in a:
    print(f"{ser} found in {a}")
else:
    print(f"{ser} not found in {a}")