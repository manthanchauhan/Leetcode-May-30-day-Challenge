class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int n = coordinates.size();
        
        if (n == 2) return true;
        
        float slope = float(coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0]);
        float c = coordinates[0][1] - slope*coordinates[0][0];
        
        // cout << slope << " " << c << endl;
         
        for (int i = 2; i < n; i ++) {
            if (abs(coordinates[i][1] - slope*coordinates[i][0] - c) <= pow(10, -9)) continue;
            else {
                // cout << abs(coordinates[i][1] - slope*coordinates[i][0]) << endl;
                return false;
            }
        }
        
        return true;
    }
};
