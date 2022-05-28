def smm():
  n = int(input("Enter number of elements : "))

  # Below line read inputs from user using map() function
  a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

  print("\nList is - ", a)
  count = 0
  for x in a:


        count=count+x
  print("summ of the list: ",count)

smm()