
def rotate(arr, n):

    last_index = n - 1
    arr1 = [0]*9

    for i in range(n):

        for j in range(n):
            arr1[i * n + last_index - j] = arr[n * j + i]

    print(*arr1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rotate(arr, 3)




