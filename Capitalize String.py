"""The program captalizes the first and last aplphabet of every word in the string"""
string1=input("enter the string that needs to be captalized: ")
string1 = result = string1.title()
result =  ""
for each_word in string1.split():

    result += each_word[:-1] + each_word[-1].upper() + " "
print(result[:-1]) 