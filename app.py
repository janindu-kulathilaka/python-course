age = 22

# Ternary Operator
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# Chaining Comparison Operators
# age should be between 18 and 65
if 18 <= age < 65:
    print("Eligible")


# for loop
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
for number in range(1, 4):
    print("Attempt", number, number * ".")
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")
