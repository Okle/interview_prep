
arr = [[0 for x in range(5)] for y in range(5)]
arr1 = [[1, 1, 0, 2, 0], [1, 0, 3, 4, 0],[1, 1, 5, 6, 2],[2, 3, 7, 6, 9],[4, 3, 3, 8, 1]]

counter = 0


def printMatrix(arr):

    for sub_arr in arr:
        print(*sub_arr)

    print()

def change_color(arr, x, y, old_color, new_color):

    global counter
    counter += 1
    if len(arr) > y >= 0 and len(arr[0]) > x >= 0:
        if arr[y][x] == old_color:
            arr[y][x] = new_color

            change_color(arr, x + 1, y, old_color, new_color)
            change_color(arr, x, y + 1, old_color, new_color)
            change_color(arr, x - 1, y, old_color, new_color)
            change_color(arr, x, y - 1, old_color, new_color)

    else:
        return

def change_color_memo(arr, x, y, old_color, new_color, memo):

    global counter
    counter += 1
    if len(arr) > y >= 0 and len(arr[0]) > x >= 0:

        if arr[y][x] == old_color:
            arr[y][x] = new_color

            key = str(x + 1) + ':' + str(y)
            if key not in memo:
                memo.add(key)
                change_color_memo(arr, x + 1, y, old_color, new_color, memo)

            key = str(x) + ':' + str(y + 1)
            if key not in memo:
                memo.add(key)
                change_color_memo(arr, x, y + 1, old_color, new_color, memo)

            key = str(x - 1) + ':' + str(y)
            if key not in memo:
                memo.add(key)
                change_color_memo(arr, x - 1, y, old_color, new_color, memo)

            key = str(x) + ':' + str(y - 1)
            if key not in memo:
                memo.add(key)
                change_color_memo(arr, x, y - 1, old_color, new_color, memo)

    else:
        return

arr = [[0 for x in range(5)] for y in range(5)]
printMatrix(arr)
counter = 0
change_color(arr, 0, 0, 0, 7)
printMatrix(arr)
print('counter: ' + str(counter))
print()

arr = [[0 for x in range(5)] for y in range(5)]
printMatrix(arr)
counter = 0
change_color_memo(arr, 2, 2, 0, 7, set())
printMatrix(arr)
print('counter: ' + str(counter))
