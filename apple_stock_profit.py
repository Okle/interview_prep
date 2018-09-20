print('Start')

# O(n^2)
def get_max_profit(stock_prices):
    # Return maximum profit from stock purchases/sales

    profit_arr = []

    for buy_index, buy_price in enumerate(stock_prices):
        for ind, sell_price in enumerate(stock_prices, start=buy_index):
            profit_arr.append(sell_price - buy_price)

    return max(profit_arr)

# O(n)
def get_max_profit_0(stock_prices):
    # Return maximum profit from stock purchases/sales
    min_price = stock_prices[0]
    max_profit = 0

    for price in stock_prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

def get_max_profit_1(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # We'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    # Start at the second (index 1) time
    # We can't sell at the first time, since we must buy first,
    # and we can't buy and sell at the same time!
    # If we started at index 0, we'd try to buy *and* sell at time 0.
    # This would give a profit of 0, which is a problem if our
    # max_profit is supposed to be *negative*--we'd return 0.
    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # Update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)

    return max_profit


stock_prices_yesterday = [10, 7, 5, 8, 11, 9, 15, 1, 69]

print(get_max_profit(stock_prices_yesterday))
print(get_max_profit_0(stock_prices_yesterday))
print(get_max_profit_1(stock_prices_yesterday))

print('End')
