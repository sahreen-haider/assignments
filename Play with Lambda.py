# program to create a lambda function that adds 25 to a given number passed in as an argument.

def n():
    r = lambda a : a + 25
    r=r(int(input('Enter the number: ')))
    print('The result is: ',r)
n()
