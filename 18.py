# 18. factorial of a given number


num = int(input("Enter the number: "))

fact = 1
for x in range(1, num + 1):
    fact *= x

print(fact)

