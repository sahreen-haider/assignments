# Write a Python class to implement pow(x, n)

import math
class pow:
    def power(self,x,n):
        lst=[x for i in range(n)]
        print("given list: ",lst)
        result=math.prod(lst)
        return result
obj=pow()
print("the result is: ",obj.power(int(input("enter the base literal : ")),int(input("enter the power for base literal : "))))