# A fruit company sells oranges for 32 cents a pound plus $7.50 per order for
# shipping. If an order is over 100 pounds, shipping cost is reduced by $1.50.
# Write a function that will take the number of pounds of oranges as a parameter
# and return the cost of the order
# 2.33
def orderCost(pounds):
    cost = 0
    oranges = 0.32
    shipping = 7.50
    if pounds < 100:
        cost = (oranges * pounds) + shipping
    elif pounds > 100:
        cost = (oranges * pounds) + (shipping - 1.50)
    print(cost)
    return cost

orderCost(77)
