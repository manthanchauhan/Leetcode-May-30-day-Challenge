class Solution 
{
    public int firstUniqChar(String s) 
    {
        int[] Freqcount = new int[26];
        for(int i = 0 ; i<s.length(); i++)
        {
            char ch = s.charAt(i);
            Freqcount[ch-'a']++;
        }
        
        for(int i = 0 ; i<s.length(); i++){
            char ch = s.charAt(i);
            if(Freqcount[ch-'a'] == 1) return i;
        }
        
        return -1;
    }
}