# time: O(N)
# extra-space: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def filld(root, d, ind):
    ans = 1
    
    if root.left is not None:
        ans += filld(root.left, d, 2*ind+1)
    
    if root.right:
        ans += filld(root.right, d, 2*ind+2)
        
    d[ind] = ans
    return ans

def kts(root, d, k, ind):
    if root.left:
        lc = d[2*ind+1]
    else:
        lc = 0
        
    if k <= lc:
        return kts(root.left, d, k, 2*ind+1)
    
    k -= lc
    
    if k == 1:
        return root.val
    
    k -= 1
    return kts(root.right, d, k, 2*ind+2)

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        d = {}
        
        filld(root, d, 0)
        
        ans = kts(root, d, k, 0)
        return ans
