size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop for columns (asterisks in each row)
    for col in range(size):
        print("*", end="")

    # Move to the next line after completing a row
    print()

    # Increment row counter
    row += 1
