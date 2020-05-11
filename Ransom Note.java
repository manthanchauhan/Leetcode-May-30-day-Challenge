class Solution {
    public boolean canConstruct(String ransomNote, String magazine) 
    {
        int[] countArr = new int[26];
        for(int i = 0 ; i<magazine.length(); i++)
        {   char ch = magazine.charAt(i);
            countArr[ch-'a']++;
        }
        
        for(int i = 0 ; i<ransomNote.length(); i++)
        {   char ch = ransomNote.charAt(i);
            if(--countArr[ch-'a']<0) return false ;
        }
        return true;
    }
}