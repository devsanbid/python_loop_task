

odd_list: list[int] = []
even_list: list[int] = []
for x in [1,2,3,4,5]:
    if x % 2 == 0:
        even_list.append(x)
    else:
        odd_list.append(x)

print(f"Odd: {odd_list}")
print(f"Even: {even_list}")
