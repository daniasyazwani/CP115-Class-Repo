correct_password = "python123"
attempts = 0
login_succesful = False

while attempts < 3:\
    password = input("Enter password")
    attempts += 1

    if password == correct_password:
        login_succesful = True
        break
    


print(login_successful)
print(attempts_used)
