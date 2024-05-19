# 33. Write a for loop which appends the type of each element in the first list to the second list.


a = [1, 2, 3, 4, 5]
b: list[type] = []
for x in a:
    b.append(type(x))
print(b)

