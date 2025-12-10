# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.
# Note: The characters in the array beyond the returned length do not matter and should be ignored.

def compressedLength(s):
    if not s:
        return 0
    n = len(s)
    i = index = 0
    
    while i<n:
        c = s[i]
        count = 0
        
        while i<n and s[i] == c:
            count += 1
            i += 1
            
        s[index] = str(c)
        index += 1
        if count > 1:
            str_count = str(count)
            for k in range(len(str_count)):
                s[index] = str_count[k]
                index +=1
                
    return index


print(compressedLength(["a","a","b","b","c","c","c"]))