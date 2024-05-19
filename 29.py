# 29. Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']


lst = ["ram", "shyam"]
result: list[str] = []
for x in lst:
    result.append(f"Dr.{x}")
print(result)
