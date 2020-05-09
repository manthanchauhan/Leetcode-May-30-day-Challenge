class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> NoteHashTable(26, 0), MagHashTable(26, 0);
        
        for (char c: ransomNote) NoteHashTable[int(c - 'a')] ++;
        
        for (char c: magazine) MagHashTable[int(c - 'a')] ++;
        
        for (int i = 0; i < 26; i ++) if (MagHashTable[i] < NoteHashTable[i]) return false;
        
        return true;
    }
};
