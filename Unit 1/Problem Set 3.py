# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

temp = '' # Stores the previous letter to be compared to
myNewString = "" # Stores the newest string to compare to the older string
myOldString = "" # The longest string so far
s += " "
for char in s:
    if char >= temp: # If the current character is greater than or equal to the previous character add that character to new string
        temp = char
        myNewString += char       
    else:
        temp = char
        if len(myNewString) > len(myOldString):
            myOldString = myNewString
            myNewString = char
        else:
            myNewString = char  
print ("Longest substring in alphabetical order is: ", myOldString)
