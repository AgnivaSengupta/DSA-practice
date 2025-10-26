# Two Sum 1
# https://leetcode.com/problems/two-sum/description/
# O(n) time and space approach using dict/hash-map
def twosum_1(arr, target):
    hashMap = {}
    for i in range(len(arr)):
        if target-arr[i] in hashMap:
            return True     
        else:
            hashMap[arr[i]] = i
            
    return False
    
arr = [2, 7, 11, 15]
target = 10

print(twosum_1(arr, target))


# Two Sum 2
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# here the input array is sorted
# The main aim here is to eliminate the O(n) extra space required in a non-sorted array approach
# Use Two Pointer for this.
def twosum_2(arr, target):
    i, j = 0, len(arr)-1
    result = []
    while i < j:
        if arr[i] + arr[j] == target:
            result.append((i+1, j+1))
            i += 1
            j -+ 1
        elif arr[i] + arr[j] > target:
            j -= 1
        else:
            i += 1
    return result
    
arr2 = [1, 2, 3, 4, 5, 6, 8, 9]
print(twosum_2(arr2, 12))