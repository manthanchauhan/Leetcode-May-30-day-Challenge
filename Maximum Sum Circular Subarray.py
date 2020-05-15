class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans1 = 0
        m_i = 0
        
        for i in range(1, len(A) + 1):
            m_i = max(m_i + A[i-1], 0)
            
            if m_i > ans1:
                ans1 = m_i
        
        if ans1 == 0:
            if 0 in A:
                return 0
            else:
                return max(A)
            
        # print(ans1)
                
        left_sum = [None]*(len(A)-1)
        left_sum[0] = A[0]
        
        for i in range(1, len(A)-1):
            left_sum[i] = left_sum[i-1] + A[i]
            
        max_right_sums = [None]*len(A)
        max_right_sums[-1] = A[-1]
        
        
        for i in range(len(A)-2, 0, -1):
            max_right_sums[i] = max_right_sums[i+1]+A[i]
            
        for i in range(len(A)-2, 0, -1):
            max_right_sums[i] = max(max_right_sums[i+1], max_right_sums[i])
            
        print(left_sum)
        print(max_right_sums)
        
        ans2 = 0
        for i in range(0, len(A)-1):
            max_sum = left_sum[i] + max_right_sums[i+1]
            ans2 = max(ans2, max_sum)
            
        return max(ans1, ans2)
            
            
        
        
        
