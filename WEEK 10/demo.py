# Get a number input from the user and convert it to an integer
number = int(input("Enter a number: "))

# Check the remainder when divided by 2
if number % 2 == 0:
    print(f"The number {number} is Even") # Even if the remainder is 0
else:
    print(f"The number {number} is Odd") # Odd if the remainder is not 0
