def calculate_arbitrage_allocation(capital, odds):
    num_outcomes = len(odds)
    assert num_outcomes >= 2, "At least two odds are required for betting."

    implied_probabilities = [1 / odd for odd in odds]
    total_implied_probability = sum(implied_probabilities)
    allocations = [(prob / total_implied_probability) * capital for prob in implied_probabilities]
    return allocations

def calculate_potential_profit(capital, odds):
    allocations = calculate_arbitrage_allocation(capital, odds)
    potential_profits = [allocations[i] * (odds[i] - 1) for i in range(len(odds))]
    return potential_profits

def calculate_profit_percentages(potential_profits, allocations):
    profit_percentages = [(profit / allocation) * 100 for profit, allocation in zip(potential_profits, allocations)]
    return profit_percentages

# Example usage for any number of odds
capital = 1000
odds = [5.1,5]
allocations = calculate_arbitrage_allocation(capital, odds)
potential_profits = calculate_potential_profit(capital, odds)
profit_percentages = calculate_profit_percentages(potential_profits, allocations)

print(f"Initial Capital: ${capital}")
print(f"Allocations: {allocations}")
print(f"Potential Profits: {potential_profits}")
print(f"Profit Percentages: {profit_percentages}")

if all(profit > 0 for profit in potential_profits):
    print("Arbitrage opportunity found!")
else:
    print("No arbitrage opportunity found.")
