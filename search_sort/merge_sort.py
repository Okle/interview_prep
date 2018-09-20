def merge_sort(list_to_sort):
    # Base case: lists with fewer than 2 elements are sorted
    if len(list_to_sort) < 2:
        return list_to_sort

    # Step 1: divide the list in half
    # We use integer division, so we'll never get a "half index"
    mid_index = len(list_to_sort) / 2
    left = list_to_sort[:mid_index]
    right = list_to_sort[mid_index:]

    # Step 2: sort each half
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Step 3: merge the sorted halves
    sorted_list = []
    while len(sorted_list) < len(list_to_sort):
        # sorted_left's first element comes next
        # if it's less than sorted_right's first
        # element or if sorted_right is empty
        if sorted_left and ((not sorted_right) or sorted_left[0] < sorted_right[0]):
            sorted_list.append(sorted_left.pop(0))
        else:
            sorted_list.append(sorted_right.pop(0))

    return sorted_list




