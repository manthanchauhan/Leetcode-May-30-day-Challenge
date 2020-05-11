/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution 
{
    //pair will contain the height and parent of the node
    class Pair
    {
        int height ;
        TreeNode par;
        Pair(int heigth, TreeNode par)
        {
            this.height = height;
            this.par = par;
        }
    }
    
    public Pair height(TreeNode root, int x)
    {   
        Pair ans = new Pair(0, null);
        
        //Find node on left side
        if(root.left!= null) 
        {
            //Node found on left
            if(root.left.val == x) return new Pair(1,root); 
            
            //Node not found on left
            //We searched in children of left
            if(ans.par==null)  ans = height(root.left, x);
        }
        
        //Find node on right side
        if(root.right!= null)
        {
            //Node found on right
            if(root.right.val == x) return new Pair(1,root); 
                    
            //Node not found on right
            //We searched in children of right
            if(ans.par==null) ans = height(root.right,x);
        }
        
        if(ans.par!=null) ans.height++;
        return ans;        
    }
    
    public boolean isCousins(TreeNode root, int x, int y) {
        
        Pair p1 = height(root,x);
        Pair p2 = height(root,y);
        
        //Parents of nodes should not be equal to null and two conditions of cousin should be fulfilled 
        if(p1.par!=null && p2.par!=null && p1.par != p2.par && p1.height == p2.height) return true;
        
        return false;
    }
}