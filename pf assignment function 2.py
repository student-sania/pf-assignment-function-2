# 1. Movie ticket prices:
def calculate_ticket_price(age, day, num_tickets):
    base_price = 10  
    
    if age == 'adult':
        price_multiplier = 1.0
    elif age == 'children':
        price_multiplier = 0.8  
    elif age == 'senior':
        price_multiplier = 0.9  
    else:
        return "Invalid age category"

    if day.lower() in ['weekday', 'weekend']:
        if day.lower() == 'weekday':
            price_multiplier *= 0.9  
        else:
            price_multiplier *= 1.2  

        if num_tickets >= 5:
            price_multiplier *= 0.8  

        total_price = base_price * price_multiplier * num_tickets
        return f"The total price for {num_tickets} {age} tickets on {day} is ${total_price:.2f}"
    else:
        return "Invalid day"
    
result = calculate_ticket_price('adult', 'weekday', 3)
print(result)        

# 2. Resturant Bill Calculator
def calculate_total_bill(items, quantities, prices, discount=0, tax_rate=0, split_count=1):
    if len(items) != len(quantities) or len(quantities) != len(prices):
        return "Error: Length mismatch in input data"

    total_cost = sum([quantities[i] * prices[i] for i in range(len(items))])

    total_cost -= total_cost * (discount / 100)

    total_cost += total_cost * (tax_rate / 100)

    if split_count > 1:
        total_cost /= split_count

    return f"The total bill amount{' after discount' if discount else ''}{' with taxes' if tax_rate else ''}{' split among friends' if split_count > 1 else ''} is ${total_cost:.2f}"

items = ["Item1", "Item2", "Item3"]
quantities = [2, 1, 3]
prices = [10, 5, 8]
discount = 10
tax_rate = 8
split_count = 3

result = calculate_total_bill(items, quantities, prices, discount, tax_rate, split_count)
print(result)

#  4. Travel Cost Estimator
def estimate_travel_cost(destination, travel_style='budget', duration=7):
    
    base_costs = {
        'budget': {'transportation': 500, 'accommodations': 50, 'activities': 30},
        'luxury': {'transportation': 1000, 'accommodations': 150, 'activities': 100}
    }

    daily_multiplier = 1.0 if duration <= 7 else 0.9  

    total_cost = sum([base_costs[travel_style][category] * duration * daily_multiplier for category in ['transportation', 'accommodations', 'activities']])

    return f"The estimated travel cost for {duration} days to {destination} ({travel_style} style) is ${total_cost:.2f}"

destination = "Paris"
travel_style = "luxury"
duration = 10

cost_estimate = estimate_travel_cost(destination, travel_style, duration)
print(cost_estimate)