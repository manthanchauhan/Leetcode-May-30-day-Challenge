class Solution {
    public int findComplement(int num) 
    {
        int temp = num;
        int mask = 1;
        
        while(temp!=0)
        {
            num ^= mask;
            mask <<= 1;
            
            temp >>= 1;
        }
        return num;
    }
}