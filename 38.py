# 38. Write a python program to display all the prime numbers within a given range.


start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

for x in range(start, end + 1):
    if x > 1:
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            print(x)

