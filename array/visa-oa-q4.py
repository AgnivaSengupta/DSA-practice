# Question:
# Given a list of height of structures. The only operation we can perform is add to the heights.
# Return the min number of operations needed to make the list such that the difference between adjacent heights is only 1

def min_operations_strictly_increasing(heights):
    n = len(heights)
    ops = 0
    prev = heights[0]

    for i in range(1, n):
        if heights[i] <= prev:
            prev += 1
            ops += prev - heights[i]
        else:
            prev = heights[i]

    return ops


heights = [1, 8, 2, 5, 11]
print(min_operations_strictly_increasing(heights))
