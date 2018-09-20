
def bubble_sort(arr):

    for i in range(len(arr)):

        count_swaps = 0
        for j in range(0, len(arr) - i - 1):

            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                count_swaps += 1

        if count_swaps == 0:
            break

    print(arr)




arr = [7, 3, 5, 8, 4, 56, 78, 9, 0]
bubble_sort(arr)

