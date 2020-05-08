/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int depth(TreeNode* root,int val,int currentdepth){
        if(root == NULL)
            return -1;
        
        if(root->val == val)
            return currentdepth;
        
        int goDown = depth(root->left,val,currentdepth + 1);
        
        if(goDown != -1)
            return goDown;
        
        goDown = depth(root->right,val,currentdepth + 1);
        return goDown; 
    }
    };
    
    int parent(TreeNode* root,int val,int par){
    if(root == NULL)
        return -1;
        
    if(root->val == val)
        return par;

        int goLeft = parent(root->left,val,root->val);
        if(goLeft != -1)
            return goLeft;
        int goRight = parent(root->right,val,root->val);
        return goRight;
    }
    
    
    bool isCousins(TreeNode* root, int x, int y) {
        int depX = depth(root,x,0);
        int depY = depth(root,y,0);
        
        if(depX != depY)
            return false;
        
        int parentX = parent(root,x,-1);
        int parentY = parent(root,y,-1);
       
        if(parentX == parentY)
            return false;
        
        if((parentX != parentY)&&(depX == depY))
            return true;
        
        return false;
        
        
    }
