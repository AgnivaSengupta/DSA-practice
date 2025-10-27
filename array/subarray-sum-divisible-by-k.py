def divisbleByK(arr, k):
    count = {0: 1}
    ps = 0
    result = 0
    
    for num in arr:
        ps += num
        rem = ps % k
        rem = (rem + k) % k # to handle negative remainders
        if rem in count:
            result += count[rem]
        count[rem] = count.get(rem, 0) + 1
    return result
    
nums = [4, 5, 0, -2, -3, 1]
k = 5
print(divisbleByK(nums, k))