inventory = 0

while True:
    user_input = input("Please enter stock quantity (or type 'quit' to quit): ")

    if user_input.lower() == 'quit':
        break

    if user_input.isdigit():
        quantity = int(user_input)
        if quantity < 0:
            print("Quantity cannot be negative. Please enter a valid number.")
            failed_entries += 1
            continue

        inventory += quantity

        print(f"Added {quantity} to inventory. Total inventory: {inventory}")
    else:
        print("Invalid input.")
        continue
