class Solution 
{
    
    public int[][] dir = {
        {0,1},
        {0,-1},
        {1,0},
        {-1,0}
    };
    
    public  void dfs(int[][]  image, int sr, int sc, int newColor,int oldColor)
    {
        if(image[sr][sc] == newColor) return;
        image[sr][sc] = newColor;
        
        int n = image.length;
        int m = image[0].length;
        
        for(int i = 0 ; i<4 ;i++)
        {
            int newR = sr+dir[i][0];
            int newC = sc+dir[i][1];
            
            if(newR>=0 && newC>=0 && newR<n && newC<m && image[newR][newC] == oldColor)
            {
                dfs(image,newR,newC,newColor, oldColor);
            }
        }
        
    }
    
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) 
    {
        dfs(image,sr,sc,newColor,  image[sr][sc]);
        return image;
    }
}
