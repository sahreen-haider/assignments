# program to create a lambda function that adds 25 to a given number passed in as an argument
nums=[]
for i in range(int(input("enter the length for the list: "))):

    nums.append(int(input("enter the elements for the list: ")))
def square_num(n):
  return n * n
  

print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))


