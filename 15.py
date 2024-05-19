
user_input = input("Enter your string: ")

int_count = 0
str_count = 0

for x in user_input:

    if x.isdigit():
        int_count +=1
    else:
        str_count += 1


print(f"total integer: {int_count}")
print(f"total string: {str_count}")
