def add_prices(basket):
    total = round(0,2)
    for key in basket:
        total = round(total, 2) + round(basket[key], 2)
        print(round(total, 2))


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
add_prices(groceries)