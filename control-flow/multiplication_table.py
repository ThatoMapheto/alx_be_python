# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the table
for i in range(1, 11):
    product = number * i
    print(f"{product} * {i} = {product}")
