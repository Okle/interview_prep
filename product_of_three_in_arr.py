
# Calculate max sum of three numbers of tha array,
# including negative numbers

def product_of_three_sorted_array(arr):

    #sort
    arr.sort(reverse=True)

    temp = list()
    temp_negative = list()
    temp_prod = 1

    for i in range(3):
        temp_prod = temp_prod * arr[i]
        temp.append(arr[i])

    for i in range(2):
        if arr[len(arr) - i - 1] < 0:
            temp_negative.append(arr[len(arr) - i - 1])

    if len(temp_negative) == 2:
        product = temp_negative[0]*temp_negative[1]*temp[0]
        if product > temp_prod:
            return product
    return temp_prod


    print(temp_negative)
    print(temp)
    print(temp_prod)

def product_of_three(arr):

    max_prod = 1

    for i in range(len(arr)-2):
        num_1 = arr[i]
        for j in range(i + 1, len(arr)-1):
            num_2 = arr[j]
            for k in range(j + 1, len(arr)):
                num_3 = arr[k]
                next_prod = num_1*num_2*num_3
                if max_prod < next_prod:
                    max_prod = next_prod

    return max_prod


my_arr = [10, 3, 5, 6, 20, -10, -4, -19, 0, -200, 3000]
print(product_of_three_sorted_array(my_arr))

print(product_of_three(my_arr))

print([0]*3)


