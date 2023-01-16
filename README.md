# Scripting_Lab
This repository contains files for Scripting Languages Laboratory, 5th Sem, ISE.

**Note** - Refer https://code.visualstudio.com/docs/datascience/jupyter-notebooks to learn about working with Jupyter Notebook in VS Code.

<h3 align = "center">PART – A </h3>
<hr>

1. **Python**: Write Python code to do the following:
      - Create list with inputs from user
      - Determine minimum and maximum elements in the list
      - Insert new element into the list
      - Delete an element from the list
      - Determine if an element is present in the list.

2. **HTML and Javascript**: Create a front end that allows the user to enter details of the item purchased (item name, item price (option), number of items bought). On clicking of the submit button, the total cost for the item purchased should be calculated and displayed. On clicking on the ‘paid’ button, appropriate alert box should be popped up.

3. **Python**: Write a python program to create a class ‘Rectangle’. This class should include a constructor to initialize the dimensions. Include a function in the class to compute the area of the rectangle. Create objects of the class and print area.

4. **Python**: Write a temperature converter python program, which is menu driven. Each such conversion logic should be defined in separate functions. The program should call the respective function based on the user’s requirement. The program should run as long as the user wishes so. Provide an option to view the conversions stored as list of tuples with attributes - from unit value, to unit value sorted by the user’s choice (from-value or to-value).

5. **Javascript**: The function Change String(str) needs to modify the string passed using the following rules:
    - Replace every letter in the string with the letter that follows it in alphabetical order (ie. Z becomes a, l becomes m).
    - Take every vowel in this new string (a, e, i, o, u) and Capitalize it.
    - Return this modified string.
    
6. **Python**: Write Python code to do the following operations:
    - Create a dictionary that contains the atomic element symbol and its name.
    - Add a unique & duplicate element into this dictionary by interacting with the user. Observe the output and justify it.
    - Display the number of atomic elements in this dictionary.
    - Ask user to enter an element to search in the dictionary. Display appropriate results.
    Rewrite this program so that these operations are inside a function called ‘AtomicDictionary’. Create another python file called “Atomic.py” and execute this function in it.

7. **Python**: Create a Python class called ‘Student’ having ‘name’, ‘age’ as attribute along with a list having the marks obtained for three subjects.
    - Create a constructor to initialize two objects of this class.
    - Create a member function called ‘display’ printing the details of a specific object
    - Ask user to enter the values for an object through an ‘accept’ member function.
    - Display these details.

8. **Python**: Create a list of 6 numbers. Use ‘list-comprehension’ to create a new list where each element in the original list is multiplied by 3. Use ‘lambda’ and ‘reduce’ function find the sum of the elements of the original list as well as the new list.

9. **Javascript**: The function LetterSurround(str) needs to find out if the string passed is an acceptable sequence by either returning true or false. The string parameter will be composed of + and = symbols with several characters between them. For the string to be true each letter must be surrounded by + symbol. Test Cases: The string will not be empty and will have at least one letter.

10. **JavaScript** – Client Side Validation**: Design a case study for a Bakery that creates and validates a HTML form at the client side using Javascript. Bakery Menu & Price calculation of items bought should be the result. Perform the necessary Client Side validation using JavaScript.

<h3 align = "center">PART – B </h3>
<hr>

1. **Python Classes**: Write a python class to reverse a sentence (initialized via constructor) word by word. 
Example: “I am here” should be reversed as “here am I”. Create instances of this class for each of the three strings input by the user and display the reversed string for each, in descending order of number of vowels in the string.

2. **Python File Handling & List Comprehension**: Write a python program to read the contents of a file (filename as argument) and store the number of occurrences of each word in a dictionary. Display the top 10 words with most number of occurrences in descending order. Store the length of each of these words in a list and display the list. Write a one-line reducefunction to get the average length and one-line list comprehension to display squares of all odd numbers and display both.

3. **Python for Data Science**: Load the Titanic dataset into one of the data structures (NumPy or Pandas) and perform the following operations.
    - Display header rows and description of the loaded dataset.
    - Remove unnecessary features (E.g. drop unwanted columns) from the dataset.
    - Manipulate data by replacing empty column values with a default value.
    Perform the following visualizations on the loaded dataset:
        - Passenger status (Survived/Died) against Passenger Class
        - Survival rate of male vs female
        - No of passengers in each age group

4. **Python for Data Science**: Load the ‘Student Performance’ dataset into one of the data structures (NumPy or Pandas) and perform the following operations.
    - Display header rows and description of the loaded dataset.
    - Remove unnecessary features (E.g. drop unwanted columns) from the dataset such as ‘lunch’ and ‘test preparation course.
    - Convert the attribute ‘race/ethnicity’ to have ‘groupA’ to be ‘Asian Students’, ‘groupB’ to be ‘African Students’ , ‘groupC’ to be ‘Afro-Asian Students’, ‘groupD’ to be ‘American Students’ and ‘groupE’ to be ‘European Students’.
    Perform the following visualizations on the loaded dataset:
        - Tally of the Number of Male & Female students who took up the ‘test preparation course’ and those who did not.
        - Total Number of Male & Female Students belonging to each student group
        - No of students who ‘failed’(less than 40), ‘second class’(between 40 & 50), ‘first class’(between 60 & 75) and ‘distinction’(above 75) in ‘Maths’, ‘Reading’ and ‘Writing’.

5. **Python for Data Science** - Perform Data Visualization on Iris Dataset
    - Load the Titanic dataset into one of the data structures (NumPy or Pandas).
    - Display header rows and description of the loaded dataset.
    - Clean the data if applicable
    - Find the average petal width of each category of IRIS Species
    - Data Visualization for:
        - How many flowers of each species exists for each value of sepal width
        - How many flowers are there whose petal width is <1, between 1 to 2 and >2
        - Tally the Iris-Versicolour and Iris-Virginica species according to the value of Sepal Width

6. **Javascript**: Design a HTML page with two textboxes and button. Let user enter a sentence in the first text box and the search string in the second. Use Javascript to perform the following operations on clicking the button
    - Display the entered text
    - Display the number of digits, white space characters and alphabets in the entered
    text
    - Check the number of occurrences of any given word.
    - Determine the position of occurrence of the search string in the given string

7. **Javascript**: Design a HTML page to accept a string in a text box on the click of a button. Use Javascript to perform the following operations
    - Add the string received to a pre-existing Javascript array named “Original_String” at its beginning
    - For each array element, use a callback function and store each one’s length in a new array named “MyLength”
    - Write a Javascript function that takes the arrays “Original_String” and “MyLength” as argument. This function filters those strings with length less than or equal to 3.

8. **Python and JavaScript**: ATM Application: Design a HTML form that displays user’s current balance, an input field to enter amount and buttons to withdraw or deposit money. Validate the form such that
    - Negative amount cannot be entered and Users cannot withdraw more than 5000 at one time
    - Users cannot withdraw amount greater than their balance and cannot deposit more than 10000 at one time. Also users can perform at most 5 transactions. Update the balance accordingly and ensure relevant data is not lost on closing the browser

9. **Python and JavaScript**: Shopping Cart Application: Design a simple Shopping Cart application which allows users to add items to their cart from a list of products. Allow users to view their cart (items and quantities of each). Ensure that items in the cart persist even after closing the application. On selecting buy, print out a bill of items in the cart. Perform any necessary validation. Demonstrate data persistence even after the browser is closed.

10. **Python**: Write a Python program to perform the following:
    - Apply histogram equalization on the given image for contrast enhancement.
    - Detect edges in the given image.
