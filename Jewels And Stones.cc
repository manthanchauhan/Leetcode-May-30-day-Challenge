class Solution {
public:
    int hash(char c) {
        if (c >= 'A' and c <= 'Z')  return 26 + c - 'A';
	    else return c - 'a';
    }
    
    int numJewelsInStones(string J, string S) {
        bool HTable[52] = {false};

        for (char c: J) {
            int key = hash(c);
            HTable[key] = true;
        }

        int ans = 0;
        for (char c: S) {
            int key = hash(c);
            if (HTable[key]) ans ++;
        }

        return ans;  
    }
};
