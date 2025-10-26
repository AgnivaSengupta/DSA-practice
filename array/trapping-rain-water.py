def water_trapped(height):
    n = len(height)
    left, right = 0, n-1
    left_max, right_max = height[left], height[right]
    water = 0
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            
    return water
    
print(water_trapped([0,1,0,2,1,0,1,3,2,1,2,1]))
    