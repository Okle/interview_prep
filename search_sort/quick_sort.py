
def quick_sort(arr):

    rec_qs(arr, 0, len(arr) - 1)


def rec_qs(arr, start, end):

    if start == end:
        return

    if start < end:
        mid_index = partition(arr, start, end)
        rec_qs(arr, start, mid_index - 1)
        rec_qs(arr, mid_index + 1, end)


def partition(alist, first, last):

   pivotvalue = alist[first]

   leftmark = first + 1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark - 1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


def partition_(arr, start, end):

    pivot = arr[start + ((end - start) // 2)]

    while start <= end:

        while start < end and arr[start] < pivot:
            start += 1

        while start < end and arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]


        if start <= end:
            start += 1
            end -= 1

    return start


arr = [1, 4, 5, 3, 7, 9, 34, 67,23,43,11,68,90,1,2,888]
#arr = [9, 5, 7, 1, 6, 4]
#arr = [0, 1, 2, 3, 4]
quick_sort(arr)
print(*arr)


def quickSort(alist):

   quickSortHelper(alist, 0, len(alist)-1)


def quickSortHelper(alist, first, last):

   if first < last:

       splitpoint = partition(alist, first, last)

       quickSortHelper(alist, first, splitpoint - 1)
       quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):

   pivotvalue = alist[first]

   leftmark = first + 1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark - 1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
