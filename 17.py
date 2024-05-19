# 17. program to print the given number is odd or even


num: list[int] = eval(input("Enter the number list: "))


for x in num:
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

