correct_password = "python123"
attempts_used = 0
login_successful = False
max_attempts = 3

while attempts_used < max_attempts:
    password = input("Enter password:")
    attempts_used += 1

    if password == correct_password:
        login_successful = True
        break # Exit immediately
    


print(login_successful)
print(attempts_used)
