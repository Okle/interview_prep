def stepPerms(n, memo):
    # count permutation of 1, 2, 3 up to sum that equals to n
    if n < 0:
        return 0
    if n == 0:
        return 1

    count = 0
    if n in memo.keys():
        count = memo[n]
    else:
        for i in range(1, 4):
            count = count + stepPerms(n - i, memo)
        memo[n] = count

    return count

print(stepPerms(4, dict())) # => 7
print(stepPerms(3, dict())) # => 4