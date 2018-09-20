def whatFlavors(cost, money):
    if len(cost) <= 1:
        print(None)

    if money <= 1:
        print(None)

    comp_tbl = dict()

    for i in range(len(cost)):
        if cost[i] in comp_tbl.keys():
            price_idx = comp_tbl[cost[i]]
            cost1 = cost[price_idx]
            cost2 = cost[i]
            if cost1 > cost2:
                print(i + 1, price_idx + 1)
            else:
                print(price_idx + 1, i + 1)
        else:
            comp_tbl[money - cost[i]] = i
    print(comp_tbl)



arr = [1, 4, 5, 3, 2]
whatFlavors(arr, 4)