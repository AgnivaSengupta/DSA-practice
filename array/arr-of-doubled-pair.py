from collections import Counter

def reorder(arr):
    count = Counter(arr)
    print(count)
    print(sorted(arr, key=abs))
    for x in sorted(arr, key=abs):
        if count[x] == 0:
            continue
        if count[2*x] < count[x]:
            return False
        count[2*x] -= count[x]
        count[x] = 0
        print(count)
    
    return True

arr = [2,1,2,1,1,1,2,2]
print(reorder(arr))