# increasing triplet
def increasingTriplet(nums):
    i, j = float("inf"), float("inf")
    for k in nums:
        if k <= i:
            i = k
        elif k <= j:
            j = k
        else:
            return True

    return False
