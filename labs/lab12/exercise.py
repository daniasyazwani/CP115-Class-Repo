# WRONG - Creates infinite loop!
number = 0

while number < 10:
    if number % 2 != 0:  # If odd
        continue  # Skips the increment below!

    print(f"Processing even number: {number}")
    number += 1  # This never executes when number is odd!