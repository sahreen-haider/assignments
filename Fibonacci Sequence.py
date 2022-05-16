# program for Fibonacci series:

print("Fibonacci sequence:")

num1=int(input("enter the first number for Fiibonacci series: "))
num2=int(input("enter the second number for Fibonacci series: "))

# taking the input for the range function here for the length of sequence.
for i in range(int(input("enter a limit to which you want to print the Fibonacci sequence: "))):
    # print the next number of a series
    print(num1,end=" ")
    # Here adding last two numbers to get next number
    result = num1 + num2

    # update the values
    num1 = num2
    num2 = result