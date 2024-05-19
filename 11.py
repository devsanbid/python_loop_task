
result: list[int | str] = []
for x in [1,2,3,4]:
    if x == 3:
        continue
    result.append(x)
    if x == 1:
        result.append("a")

print(result)
