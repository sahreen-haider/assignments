str1 = input("enter the string1: ")
str2 = input("enter the string2: ")

if (len(str1) != len(str2)):
    print("Second string is not a rotation of first string")
else:
    try:
        # Concatenate str1 with str1 and store it in str1
        str1 = str1 + str1

        # Check whether str2 is present in str1
        if (str1.index(str2)):
            print("Second string is a rotation of first string")
    except ValueError:
        print("Second string is not a rotation of first string")