# Equilibrium point
#
def pivotIndex(nums):
    total = sum(nums)
    cs = 0
    for i in range(len(nums)):
        if cs == total - cs -nums[i]:
            return i
        cs += nums[i]
    return -1