# Shopping list and prices
items = ("milk","bread","eggs")
price = {"milk":1.5,"bread":2.0,"eggs":3.0}
total = 0.0
for i in range(len(items)):
    total += price[items[i]]
else:
    print("purchased items:", items)
    print("Total price:", total)
    