# "Sum of Even Numbers After Queries'
# https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

def sumEven(nums, queries):
    # evenSum = 0
    # for num in nums:
    #     if num%2 == 0:
    #         evenSum += num
    # result = []
    # for val, index in queries:
    #     if nums[index] % 2 != 0: #the number was odd -->> no contribution to evenSum
    #         if (nums[index] + val)%2 == 0:
    #            evenSum += nums[index]+val 
    #            result.append(evenSum)
    #         else:
    #            result.append(evenSum)
    #     else:
    #        if (nums[index]+val) %2 == 0:
    #           evenSum += val
    #           result.append(evenSum)
             
    #        else:
    #            evenSum -= nums[index]
    #            result.append(evenSum)
    #     # result.append(evenSum)
    #     nums[index] = nums[index] + val
    # return result
    evenSum = sum(num for num in nums if num % 2 == 0)
    result = []
            
    for val, index in queries:
        if nums[index] % 2 == 0:
            evenSum -= nums[index]

        nums[index] += val

        if nums[index] % 2 == 0:
            evenSum += nums[index]
    
        result.append(evenSum)
            
    return result
   
nums = [1, 2, 3, 4] 
queries = [[1,0],[-3,1],[-4,0],[2,3]]

print(sumEven(nums, queries))

# [1, 2, 3, 4] -> sum = 6
# loop 1 -> [2, 2, 3, 4] -> sum = 8 -> [8]
# loop 2 -> [2, -1, 3, 4] -> sum = 6 -> [8, 6]
# loop 3 -> [-2, -1, 3, 4] -> sum = 2