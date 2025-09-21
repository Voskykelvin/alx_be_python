length = int(input("Enter the size of the pattern: "))

row = 0

# While loop for rows
while row < length:
    # For loop for columns
    for col in range(length):
        print("*", end="")  # Print stars side by side
    print()  # Move to the next line after each row
    row += 1
