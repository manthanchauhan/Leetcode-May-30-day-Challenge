def isana(win, mp):
    for i in range(0, 26):
        if win[i] != mp[i]:
            return False
    
    return True


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = s2
        p = s1
        
        ns = len(s)
        np = len(p)
        
        if ns < np:
            return []
        
        s = [c for c in s]
        p = [c for c in p]

        mp = [0]*26
        
        for c in p:
            mp[ord(c) - 97] += 1
        
        win = [0]*26
        
        for i in range(0, np):
            win[ord(s[i]) - 97] += 1
            
        if isana(win, mp):
            return True
            
        for i in range(1, ns - np + 1):
            win[ord(s[i-1]) - 97] -= 1
            win[ord(s[np + i -1]) - 97] += 1
            
            if isana(win, mp):
                return True
                
        return False
        
