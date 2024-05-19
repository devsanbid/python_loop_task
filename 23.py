# 23. Python program to count the space of a given string


string = input("Enter the string: ")
count = 0
for x in string:
    if x == " ":
        count += 1
print(count)


