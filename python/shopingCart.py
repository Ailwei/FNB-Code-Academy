foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to Quit: ")
    if food.lower() == 'q':
        break
    else:
        try:
            price = float(input(f"Enter the price of the {food} (R): "))
        except ValueError:
            print("Invalid price! Please enter a number.")
            continue
        
        foods.append(food)
        prices.append(price)
        total += price
        print(f"Added {food} costing R{price:.2f} to your cart.\n")

print("\nYour shopping cart summary:")
for i in range(len(foods)):
    print(f"- {foods[i]}: R{prices[i]:.2f}")

print(f"\nTotal amount to pay: R{total:.2f}")
print("Thank you for shopping!")
