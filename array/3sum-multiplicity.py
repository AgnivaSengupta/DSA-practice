from typing_extensions import Counter

def threeSumMulti(arr, target):
    MOD = 10**9 + 7
    count = Counter(arr)
    keys = sorted(count)
    ans = 0
    
    for i, x in enumerate(keys):
        for j, y in enumerate(keys[i:], i):
            z = target - x - y
            if z not in count:
                continue
            # Case 1: all same
            if x == y == z:
                ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
            # Case 2: two same
            elif x == y != z:
                ans += count[x] * (count[x] - 1) // 2 * count[z]
            elif x < y < z:
                ans += count[x] * count[y] * count[z]
    return ans % MOD
    
arr = [1,1,2,2,3,3,4,4,5,5]
target = 8

print(threeSumMulti(arr, target))