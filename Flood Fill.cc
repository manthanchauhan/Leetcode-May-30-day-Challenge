class Solution {
public:
    int oldc;
    
    void fill(vector<vector<int>>& image, int sr, int sc, int colr, int tr, int tc) {
        if (image[sr][sc] == colr) return;
        
        image[sr][sc] = colr;
        
        if (sc + 1 < tc and image[sr][sc+1] == oldc) {
            fill(image, sr, sc+1, colr, tr, tc);
        }
        
        if (sc - 1 >= 0 and image[sr][sc-1] == oldc) {
            fill(image, sr, sc-1, colr, tr, tc);
        }
        
        if (sr - 1 >= 0 and image[sr-1][sc] == oldc) {
            fill(image, sr-1, sc, colr, tr, tc);
        }
        
        if (sr + 1 < tr and image[sr+1][sc] == oldc) {
            fill(image, sr+1, sc, colr, tr, tc);
        }
        
        return;
    }
    
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int row = image.size();
        int col = image[0].size();
        oldc = image[sr][sc];
        
        fill(image, sr, sc, newColor, row, col);   
        return image;
    }
};
