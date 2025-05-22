# Take user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Check voting eligibility
if age >= 18:
    print(f"Hello {name}, Congratulations! You are now eligible to vote.")
else:
    print(f"Sorry {name}, you are not eligible to vote.")
