# 39. given number is prime or not


num = int(input("Enter the number: "))

for x in range(2, num):
    if num % x == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")
