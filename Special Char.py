# Program to check if a string contains any special character.
import re
string=input("enter the given string that needs to be checked for: ")
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if(regex.search(string) == None):
    print("String is accepted")
else:
    print("String is not accepted")
