# 16. Python program to check the validity of username and password input by users

import os

user_name = input("Enter your user name: ")
password = input("Enter your password: ")


attempt = 0
total_attempt = 3

while True:
    if user_name == "admin" and password == "admin123":
        print("Login Success")
        break
    else:
        attempt += 1
        _ = os.system("clear")
        print(
            f"Invalid user name or password. You have {total_attempt - attempt} attempt left"
        )
        user_name = input("Enter your user name: ")
        password = input("Enter your password: ")

    if attempt == total_attempt:
        print("Your account has been blocked")
        break
