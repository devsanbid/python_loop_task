
num_list: list[int] = []
str_list: list[str] = []


for x in [1,2,3,"d",4,5,"e"]:
    if isinstance(x,int):
        num_list.append(x)
    if isinstance(x,str):
        str_list.append(x)

print(f"num: {num_list}")
print(f"str: {str_list}")
