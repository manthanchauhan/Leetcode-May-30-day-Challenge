//using own Hashing
class Solution 
{
    public int hash(char key)
    {
        if (key >= 'A' && key <= 'Z')  return 26 + key - 'A';
	      else return key - 'a';
    }

    public int numJewelsInStones(String J, String S) 
    {
        int[] HashMap = new int[52];
        
        for(int i = 0 ; i<J.length() ; i++)
        {
            char ch = J.charAt(i);
  
            int hashIdx = hash(ch);          
            HashMap[hashIdx] = 1;    
        }
        
        int count = 0;
        
        for(int i = 0 ; i<S.length() ; i++)
        {
            char ch = S.charAt(i);

            int hashIdx = hash(ch);
            if( HashMap[hashIdx]==1) count++;
        }
        return count;   
    }
}


//Using inbuilt HashSet
// class Solution {
//     public int numJewelsInStones(String J, String S) 
//     {
//         HashSet<Character> hs = new HashSet<>();
//         for(int i = 0 ; i<J.length() ; i++)
//         {
//             char ch = J.charAt(i);
//             hs.add(ch);
//         }
//         int count = 0;
//         for(int i = 0 ; i<S.length() ; i++)
//         {
//             char ch = S.charAt(i);
//             if(hs.contains(ch)) count++;
//         }
//         return count;
//     }
// }