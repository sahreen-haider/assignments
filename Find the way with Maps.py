# program to triple all numbers of a given list of integers. Use Python map.
nums=[]
for i in range(int(input("enter the length of list: "))):
    
    nums.append(int(input("enter the elements for the list: ")))

print("Original list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of said list numbers:")
print(list(result))


