# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

a=0
b=3
bobcount = 0
bob = 'bob'

while (b != (len(s)+1)):    
    if (s[a:b]).count(bob):
        bobcount += 1
    a += 1
    b += 1

print ("Number of times bob occurs is: ", bobcount)
