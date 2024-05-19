# 21. Python program to calculate the sum of all the odd numbers within the given range.


start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

sum = 0
for x in range(start, end + 1):
    if x % 2 != 0:
        sum += x
print(sum)

