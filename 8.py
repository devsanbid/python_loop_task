
result: list[int] = []
for x in [1,2,3,4]:
    if x == 1:
        continue
    result.append(x)

    if x == 4:
        result.append(5)

print(result)

