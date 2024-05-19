# 37. Python program to count the number of even and odd numbers from a series of numbers.


numbers: list[int] = eval(input("Enter the numbers: "))
count_odd = 0
count_even = 0
for x in numbers:
    if not x % 2:
        count_even += 1
    else:
        count_odd += 1
print("Number of even numbers :", count_even)
print("Number of odd numbers :", count_odd)


