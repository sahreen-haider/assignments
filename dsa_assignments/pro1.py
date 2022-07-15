arr_lst=[]
summ=0
n_l=0
def count():

	count = 0

	for i in range(0, n_l):
		for j in range(i + 1, n_l):
			if arr_lst[i] + arr_lst[j] == summ:
				count += 1

	return count

for x in range(int(input("enter the length: "))):
	arr_lst.append(int(input("input the literals: ")))

n_l = len(arr_lst)
sum = int(input("enter the sum that you wish to find: "))
print("Count of pairs is",count())