# ======================================================================================================================================================================================+
# RESTORE IP ADDRESS                                                                                                                                                                    |
# ======================================================================================================================================================================================+
# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. 
# You may return the valid IP addresses in any order.

def restoreIp(s):
    def isValid(substr):
        if int(substr)<=255 and int(substr) >= 0 and substr[0] != '0':
           return True
        return False
        
    res = []
    n = len(s)
    if n > 12:
        return []
    
    def backTrack(s, index , parts):
        if len(parts) == 4 and index == n:
            res.append(".".join(parts))
            return
            
        for i in range(1, 4):
            if index + i > n:
                break
            
            segment = s[index:index+i]
            
            if i > 1:
                if not isValid(segment):
                    continue
                    
            parts.append(segment)
            backTrack(s, index+i, parts)
            parts.pop()
            
    backTrack(s, 0, [])
    
    return res
    
print(restoreIp("1111111"))