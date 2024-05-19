# 30. Write a for loop which appends the square of each number to the new list.


lst: list[int] = eval(input("Enter the list: "))
result: list[int] = []
for x in lst:
    result.append(x**2)
print(result)
