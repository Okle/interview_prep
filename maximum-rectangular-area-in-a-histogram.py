# largest-rectangle-under-histogram


# The stack maintain the indexes of buildings with ascending height.
# Before adding a new building pop the building who is taller than the new one.
# The building popped out represent the height of a rectangle with the new building as
# the right boundary and the current stack top as the left boundary.
# Calculate its area and update ans of maximum area. Boundary is handled using dummy buildings.
def largestRectangleArea(height):

    height.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans

arr = [6, 2, 5, 4, 5, 1, 6]

# print(largestRectangleArea(arr))
#
# def findMaxArea(arr):
#
#     tot_max = 0
#     stack = list()
#     for i in range(1, len(arr)):
#
#         if len(stack) == 0 or arr[i] >= arr[stack[-1]]:
#             stack.append(i)
#
#         else:
#
#             top_index = stack[-1]
#             h = arr[top_index]
#
#             while h > arr[i] and len(stack) > 0:
#                 stack.pop()
#                 top_index = stack[-1]
#                 h = arr[top_index]
#
#             if len(stack) == 0:
#                 curr_max_area = arr[i] * ( i + 1)
#             else:
#                 curr_max_area = h *  (i + 1)
#
#             tot_max = max(tot_max, curr_max_area)
#
#
#
#
#             # Calculate the area with h stack as smallest bar
#             # area_with_top = h * (s.empty() ? i: i - s.peek() - 1);
#
#             area = list()
#             curr_min = arr[0]
#             area.append(arr[0])
#
#
#
#         if arr[i] < curr_min:
#





