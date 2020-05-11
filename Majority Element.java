class Solution 
{
    public int majorityElement(int[] nums) 
    {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        int len = nums.length;
        
        for(int n: nums)
        {
            int count =  map.getOrDefault(n,0);
            count++;
            
            map.put(n,count);
            
            //As soon as the count of number increases by half of numbers in array; we return the number.
            if(count>(len/2)) return n;
        }
        return -1;
    }
}