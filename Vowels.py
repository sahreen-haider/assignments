"""The program to count the number of vowels in a string entered by the user"""
string_input=input("Enter string for which the vowels need to be counted: ")
print("Given string: ",string_input)
count_vowels=0
for i in string_input:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            count_vowels=count_vowels+1
print("Count of vowels in the string are:")
print(count_vowels)
