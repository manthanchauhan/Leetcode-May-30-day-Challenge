def minf(beg, end, num):
    val = num[end]
    i = end
    
    for ind in range(end-1, beg-1, -1):
        if num[ind] <= num[i]:
            i = ind
    
    return i

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        beg = 0
        n = len(num)
        ind = k
        ans = ""
        
        while ind < n:
            beg = minf(beg, ind, num)+1
            # print(beg-1)
            ans += num[beg-1]
            ind += 1
            
        if ans == '':
            return "0"
        
        return str(int(ans))
