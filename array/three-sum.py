# Three Sum
# https://leetcode.com/problems/3sum/description/
# arr[i] + arr[j] + arr[k] = 0 ==> arr[i] + arr[j] = arr[k]
# Time complexity --> O(n^2)


def threeSum(arr):
    n = len(arr)
    if n < 3:
        return []
    arr.sort()
    result = []
    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left, right = i + 1, n - 1

        while left < right:
            s = arr[left] + arr[right]
            if s == -arr[i]:
                result.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif s < -arr[i]:
                left += 1
            else:
                right -= 1

    return result


print(threeSum([-2,0,1,1,2]))

# -2 0 1 1 2
#  i l     r
#  i   l r
#    i l   r