

def merge_ranges(arr):

    merged = list()

    for i in range(len(arr) - 1):

        start = arr[i][0]
        end = arr[i][1]

        isStartMerged = False
        isEndMerged = False

        for j in range(i, len(arr)):

            curr_start = arr[j][0]
            curr_end = arr[j][1]

            if not isStartMerged and curr_start <= start <= curr_end:
                start = curr_start
                isStartMerged = True

            if not isEndMerged and curr_start <= end <= curr_end:
                end = curr_end
                isEndMerged = True

            if isEndMerged and isStartMerged:
                break


        merged.append((start, end))

    return merged


arr = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print(merge_ranges(arr))

# [(0, 1), (3, 8), (9, 12)]