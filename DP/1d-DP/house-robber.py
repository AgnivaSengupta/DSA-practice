# the state transition eq:
# Here i is the number of house in consideration.
# hence the final value is dp[n]
# dp[i] = max(num[i]+dp[i-2], dp[i-1])
# dp[i-1] --> the ith house is not taken. The value till the i-1th house is kept
# dp[i-2] + num[i] --> the ith house is taken and as a result the i-1th house is not taken

def rob1(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
        
    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], (nums[i] + dp[i-2]))
    
    return dp[n-1]


# ============================================================================
# Space Optimized version
# ============================================================================

def rob_optimized(nums):
    n = len(nums)
    if n == 0:
        return 0
        
    if n == 1:
        return nums[0]
        
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    for i in range(2, n):
        curr = max(prev1, nums[i]+prev2)
        prev2 = prev1
        prev1 = curr
        
    return prev1
    
nums = [2, 7, 9, 3, 1]  
print(rob_optimized(nums))


# ============================================================================
# Home Robber 2 --> Circular Array
# ============================================================================

def rob2(nums):
