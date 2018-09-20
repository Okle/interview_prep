fib_res = set()
fib_res.add(1)
fib_res.add(2)
fib_arr = list()
fib_arr.extend([1, 2])



def isFib(num):
    if num in fib_res:
        return True

    updateFib(num)

    if num in fib_res:
        return True

    return False


def updateFib(num):
    if num > fib_arr[-1]:
        a = fib_arr[-2]
        b = fib_arr[-1]
        fib_num = 0
        while fib_num <= num:
            fib_num = a + b
            fib_arr.append(fib_num)
            fib_res.add(fib_num)
            a = b
            b = fib_num




arr = [1, 3, 7, 3, 2, 2, 1, 7, 3, 1, 7, 1, 6]
n = len(arr)
result = list()
start = 0
end = n - 1
max_count = 0

count = 0
for i in range(len(arr)):
    if isFib(arr[i]):
        count += 1
    else:
        if count != 0 and max_count < count:
            max_count = count
            start = i - count
            end = i - 1
        count = 0

for i in range(start, end + 1):
    result.append(arr[i])

print(*result)

#
# Input:
# 37
# 1 3 7 7 7 3 2 2 2 7 3 1 7 1 6 3 5 5 4 5 6 2 1 2 4 7 3 1 3 5 4 1 7 2 6 1 2
#
# Its Correct output is:
# 1 3 3 2 2 2 3 1 1 3 5 5 5 2 1 2 3 1 3 5 1 2 1 2
#
# And Your Code's output is:
# 1 3 7 7 7 3 2 2 2 7 3 1 7 1 6 3 5 5 4 5 6 2 1 2 4 7 3 ...