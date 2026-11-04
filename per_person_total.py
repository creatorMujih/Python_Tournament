purchases = [
    {"customer": "Alice", "item": "Rice", "price": 2500},
    {"customer": "Bob", "item": "Milk", "price": 1500},
    {"customer": "Alice", "item": "Bread", "price": 1200},
    {"customer": "Bob", "item": "Eggs", "price": 2000},
    {"customer": "Alice", "item": "Sugar", "price": 800},
    {"customer": "Charlie", "item": "Oil", "price": 3000},
    {"customer": "Bob", "item": "Bread", "price": 1000}
]

# Calculate total spending per customer
totals = {}

for purchase in purchases:
    customer = purchase["customer"]
    price = purchase["price"]

    if customer not in totals:
        totals[customer] = 0

    totals[customer] += price

# Display results
for customer, total in totals.items():
    print(customer, ":", total)
