# Pangram --> a sentence that contains all the letters in english at least once
# 
# def checkPangram(s):
#     seen = set()
#     for c in s:
#         if c.lower() in seen:
#             return False
#         seen.add(c)
#     return True
    

# word1 = "cabbba", word2 = "abbccc"
# c-> 1             c-> 3  --- c-> 1 --- c-> 1
# a-> 2             a-> 1  --- a-> 3 --- a-> 2
# b-> 3             b-> 2  --- b-> 2 --- b-> 3
# 
# if the frequency can be swapped to that they are equal --> then also True
from collections import Counter


def sol(word1, word2):
    if len(word1) != len(word2):
        return False

    c1 = Counter(word1)
    c2 = Counter(word2)
    
    if set(c1.keys()) != set(c2.keys()):
        return False
        
    else:
        return sorted(c1.values()) == sorted(c2.values())
        
        
def detectCapitalUse(word: str) -> bool:
    count = 0
    for c in word:
        if c<'a'  or c > 'z':
            count += 1

    if len(word) == count or count == 0 or (count ==1 and word[0].isupper()):
        print(count)
        return True

    else:
        return False
        
print(detectCapitalUse("FlaG"))