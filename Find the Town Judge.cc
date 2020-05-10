class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        set<int> possjudges;
        vector<int> votes(N+1, 0);
        
        
        for (int i = 1; i <= N; i ++) possjudges.insert(i);
        
        for (vector<int> v: trust) {
            int src = v[0];
            int tar = v[1];
            
            possjudges.erase(src);
            votes[tar] ++;
        }
        
        set<int>::iterator itr;
        
        for (itr = possjudges.begin(); itr != possjudges.end(); itr ++) {
            int tempj = *itr;
            
            if (votes[tempj] == N-1) return tempj;
        }
        
        return -1;
        
    }
};
