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

def calculate_profit_percentage(capital, odds):
    allocations = calculate_arbitrage_allocation(capital, odds)
    total_allocation = sum(allocations)
    profit_percentage = sum(calculate_potential_profit(capital, odds)) / total_allocation * 100
    return profit_percentage

# Example usage for any number of odds
capital = 10000
odds = [2.5, 2.8, 3.2]
allocations = calculate_arbitrage_allocation(capital, odds)
potential_profits = calculate_potential_profit(capital, odds)
profit_percentage = calculate_profit_percentage(capital, odds)
total_profit = sum(potential_profits)

print(f"Initial Capital: ${capital}")
print(f"Allocations: {allocations}")
print(f"Potential Profits: {potential_profits}")
print(f"Profit Percentage: {profit_percentage:.2f}%")
print(f"Total Profit: {total_profit}%")
