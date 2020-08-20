while True:
    num_of_items = int(input("Number of items: "))
    if num_of_items < 0:
        print("Invalid numberof items!")
        continue
    total = 0
    for i in range(0, num_of_items):
        total += float(input("Price of item: "))
    discount = 0
    if total > 100:
        discount = 0.1
    total_price = total - (total * discount)
    print(f"Total price for {num_of_items} is ${total_price:.2f}")