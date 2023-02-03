def sort_by_second_last_char(s):
    return s[-2]

given_list = []
for each in range(int(input("please enter the number of items to put in the list"))):
    given_list.append(input("please enter the data here: "))
sorted_list = sorted(given_list, key=sort_by_second_last_char)
print(sorted_list)