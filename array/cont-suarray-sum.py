def checkSubarraySum(nums, k):
    dic = {0: -1}
    summ = 0
    for i, val in enumerate(nums):
        summ += val
        modulo = summ % k
        print(f"{i} --> {summ} --> {modulo}")
        if modulo in dic and abs(dic[modulo] - i) >= 2:
            print(dic)
            return True
        elif modulo in dic and abs(dic[modulo] - i) < 2:
            continue
        else:
            dic[modulo] = i

    print(dic)
    return False
    
nums = [23,2,6,4,7]
k = 6
print(checkSubarraySum(nums, k))
