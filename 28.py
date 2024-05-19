# 28. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam


a = ["ram", "shyam", 1, 2]
for x in a:
    if isinstance(x,str):
        print(f"Hello!, {x}")

