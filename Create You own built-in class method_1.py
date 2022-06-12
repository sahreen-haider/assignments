# Write a Python class to implement pow(x, n)

class pow:
    def __int__(self,x,n):
        result=x**n
        return result

obj=pow()
print("the result is :",obj.__int__(int(input("enter the base literal : ")),int(input("enter the power for base literal : "))))

