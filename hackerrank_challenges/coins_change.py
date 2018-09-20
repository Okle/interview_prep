

# Complete the ways function below.
def ways_iter(n, coins):

    if n == 0:
        return 1

    if len(coins) == 0:
        return 0

    amount = [0] * (n + 1)
    amount[0] = 1

    for coin in coins:
        for i in range(1, n + 1):
            if i >= coin:
                amount[i] = amount[i] + amount[i - coin]

    return amount[n]

def ways_rec(n, coins, index):

    if n == 0:
        return 1

    if index >= len(coins):
        return 0

    count = 0
    amount_with_coins = 0

    while amount_with_coins <= n:
        count = count + ways_rec(n - amount_with_coins, coins, index + 1)
        amount_with_coins += coins[index]

    return count

def ways_memo(n, coins, index, memo):
    if n == 0:
        return 1

    if index >= len(coins):
        return 0

    ways_count = 0
    amount_with_coins = 0

    while amount_with_coins <= n:
        ways_count += ways_memo(n - amount_with_coins, coins, index + 1, memo)
        amount_with_coins += coins[index]

    return ways_count

def ways(n, coins, i):

    if n == 0:
        return 1

    if n < 0 or i >= len(coins):
        return 0

    count = 0
    coins_sum = 0

    while coins_sum <= n:
        count = count + ways(n - coins_sum, coins, i + 1)
        coins_sum = coins_sum + coins[i]

    return count


coins = [1, 2, 3, 4]
n = 4
print(ways_iter(n, coins))
print(ways_memo(n, coins, 0, dict()))
print(ways_rec(n, coins, 0))
print(ways(n, coins, 0))