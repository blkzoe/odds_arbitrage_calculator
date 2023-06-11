def calculate_arbitrage_allocation(capital, odds, is_three_way=False):

    if is_three_way:

        assert len(odds) == 3, "Three odds are required for three-way betting."

        implied_probabilities = [1 / odd for odd in odds]

        total_implied_probability = sum(implied_probabilities)

        allocations = [(prob / total_implied_probability) * capital for prob in implied_probabilities]

        return allocations

    else:

        assert len(odds) == 2, "Two odds are required for two-way betting."

        implied_probabilities = [1 / odd for odd in odds]

        total_implied_probability = sum(implied_probabilities)

        allocations = [(prob / total_implied_probability) * capital for prob in implied_probabilities]

        return allocations

def calculate_potential_profit(capital, odds, is_three_way=False):

    allocations = calculate_arbitrage_allocation(capital, odds, is_three_way)

    if is_three_way:

        potential_profits = [allocations[i] * (odds[i] - 1) for i in range(3)]

        return potential_profits

    else:

        potential_profit = sum(allocations) * (max(odds) - 1)

        return potential_profit

# Example usage for two-way odds

capital = 10000

odds = [2.5, 2.8]

allocations = calculate_arbitrage_allocation(capital, odds)

potential_profit = calculate_potential_profit(capital, odds)

print(f"Allocations: {allocations}")

print(f"Potential Profit: {potential_profit}")

# Example usage for three-way odds

capital = 10000

odds = [2.5, 3.0, 4.0]

allocations = calculate_arbitrage_allocation(capital, odds, is_three_way=True)

potential_profits = calculate_potential_profit(capital, odds, is_three_way=True)

print(f"Allocations: {allocations}")

print(f"Potential Profits: {potential_profits}")

