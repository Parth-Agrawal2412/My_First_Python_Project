def bill_generator():
    print("Welcome to the Bill generator made by Parth Agrawal")
    try:
        item_value = int(input("Enter how many Items do you want to add in your bill: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    items, unit_prices, quantities, costs = [], [], [], []

    for _ in range(item_value):
        try:
            input_item = input("Enter your item name: ")
            input_cost = float(input(f"Enter cost of {input_item}: "))
            input_quantity = int(input(f"Enter the quantity of {input_item}: "))
        except ValueError:
            print("Invalid input type entered. Skipping remaining inputs.")
            return

        items.append(input_item)
        unit_prices.append(input_cost)
        quantities.append(input_quantity)
        costs.append(input_cost * input_quantity)

    total_amount = sum(costs)
    total_items = sum(quantities)

    try:
        discount = float(input("Enter discount in percentage(%), if none enter 0: "))
    except ValueError:
        discount = 0.0

    total_discount = (total_amount * discount) / 100
    final_amount = total_amount - total_discount

    print(f"The total amount to be paid is {final_amount:.2f}")
    choice = input("Do you want to print bill (y / n): ")
    if choice.lower() == "y":
        print("\n" + "-" * 55)
        print(f"{'S.No':<5} {'Item Name':<20} {'Price':<10} {'Qty':<8} {'Total':<10}")
        print("-" * 55)

        for index in range(len(items)):
            print(f"{index + 1:<5} {items[index]:<20} {unit_prices[index]:<10.2f} {quantities[index]:<8} {costs[index]:<10.2f}")

        print("-" * 55)
        print(f"Total Amount: {total_amount:.2f}")
        print(f"Total Items:  {total_items}")
        print(f"Discount:     {total_discount:.2f}")
        print(f"Final Amount: {final_amount:.2f}")
        print("-" * 55)


if __name__ == "__main__":
    bill_generator()