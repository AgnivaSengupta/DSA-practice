#  Pairs of Songs With Total Durations Divisible by 60
# 
# 
def numPairsDivisibleBy60(time):
    count = [0] * 60
    res = 0
    for t in time:
        rem = t % 60
        complement = (60 - rem) % 60
        res += count[complement]
        count[rem] += 1
    return res

time = [30,20,150,100,40]

print(numPairsDivisibleBy60(time))