class StockSpanner:

    def __init__(self):
        self.p = []
        self.n = 0
        self.a = []

    def next(self, price: int) -> int:
        self.p.append(price)
        self.n += 1
        
        if self.n == 1:
            self.a.append(1)
            return self.a[-1]
        
        ans = 1
        p = self.n - 2
        
        while p >= 0:
            # print(p, self.p, self.a)
            if self.p[p] <= self.p[-1]:
                ans += self.a[p]
                
                p -= self.a[p]
            else:
                self.a.append(ans)
                return ans
        
        self.a.append(ans)
        return ans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
