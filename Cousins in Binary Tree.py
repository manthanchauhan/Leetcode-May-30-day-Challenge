# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def depth_n_parent(root, depth, x):
    if (root.left is not None) and (root.left.val == x):
        return (depth+1, root.val)
        
    if (root.right is not None) and (root.right.val == x):
        return (depth+1, root.val)
    
    ans = None
    
    if root.left is not None:
        ans = depth_n_parent(root.left, depth+1, x)
        
    if (ans is None) and (root.right is not None):
        ans = depth_n_parent(root.right, depth+1, x)
        
    return ans
    
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool: 
        if root.val == x or root.val == y:
            return False
        
        xd, xp = depth_n_parent(root, 0, x)
        yd, yp = depth_n_parent(root, 0, y)
        
        # print(xd, xp, yd, yp)
        
        if (xd == yd) and (xp != yp):
            return True
        
        return False
        
