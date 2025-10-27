from collections import defaultdict

def subarraySum(nums, k):
    ps = 0
    count = defaultdict(int)
    count[0] = 1
    result = 0
    
    for num in nums:
        ps += num
        result += count[ps - k]
        count[ps] += 1
    return result

nums = [3, 4, -7, 1, 3, 3, 1, -4]
k = 7
print(subarraySum(nums, k))