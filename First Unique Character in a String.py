class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = [0]*26
        
        for c in s:
            counts[ord(c) - ord('a')] += 1
            
        for i in range(0, len(s)):
            if counts[ord(s[i]) - ord('a')] == 1:
                return i
            
        return -1
        
