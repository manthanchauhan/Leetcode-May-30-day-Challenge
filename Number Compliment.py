class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        value = 1
        
        while num:
            bit = num%2
            num //= 2
            
            ans += (not bit)*value
            value *= 2
            
        return ans
        
