
def merge_lists(first_list, second_list):

    merged_list = []
    first_index = 0
    second_index = 0

    while first_index < len(first_list) or second_index < len(second_list):

        if first_index < len(first_list) and (second_index >= len(second_list) or first_list[first_index] <= second_list[second_index]):
            merged_list.append(first_list[first_index])
            first_index += 1
        elif second_index < len(second_list):
            merged_list.append(second_list[second_index])
            second_index += 1

    return merged_list


def merge_sorted_arr(nums1, m, nums2, n):
    # Start from the end of both arrays
    ptr_m, ptr_n = m - 1, n - 1
    ptr_end = (m + n) - 1

    while ptr_m >= 0 and ptr_n >= 0:
        if nums1[ptr_m] > nums2[ptr_n]:
            nums1[ptr_end] = nums1[ptr_m]
            ptr_m -= 1
        else:
            nums1[ptr_end] = nums2[ptr_n]
            ptr_n -= 1
        ptr_end -= 1

    if ptr_n >= 0:
        while ptr_n >= 0:
            nums1[ptr_end] = nums2[ptr_n]
            ptr_n -= 1
            ptr_end -= 1


def merge_lists_1(first_list, second_list):
    # Set up our merged_list
    merged_list_size = len(first_list) + len(second_list)
    merged_list = [None] * merged_list_size

    current_index_second = 0
    current_index_first = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        is_first_list_exhausted = current_index_first >= len(first_list)
        is_second_list_exhausted = current_index_second >= len(second_list)
        if (not is_first_list_exhausted and
                (is_second_list_exhausted or
                 first_list[current_index_first] < second_list[current_index_second])):
            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list
            merged_list[current_index_merged] = first_list[current_index_first]
            current_index_first += 1
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = second_list[current_index_second]
            current_index_second += 1

        current_index_merged += 1

    return merged_list


my_list = [3, 4, 11, 15, 18]
his_list = [1, 5, 8, 12, 14, 16, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists_1(my_list, his_list))

