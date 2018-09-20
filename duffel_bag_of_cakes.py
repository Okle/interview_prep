cake_tuples = [(7, 160), (3, 90), (2, 15), (0, 0)]
capacity = 20


# Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
def max_duffel_bag_value(cake_tuples, capacity):

    price_per_kilo = []

    for cake in cake_tuples:
        if cake[0] > 0 :
            price_per_kilo.append((cake[1]/cake[0], cake[0], cake[1]))

    def take_first(elem):
        return elem[0]

    price_per_kilo_sorted = sorted(price_per_kilo, reverse=True, key=take_first)

    print(price_per_kilo_sorted)

    current_capacity = 0
    value = 0

    for cake_data in price_per_kilo_sorted:

        if current_capacity < capacity and cake_data[1] <= capacity - current_capacity:
            count = (capacity - current_capacity)//cake_data[1]
            current_capacity = cake_data[1] * count
            value = value + cake_data[2] * count


    return value


print(max_duffel_bag_value(cake_tuples, capacity))

