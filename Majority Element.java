//Solution 1
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

//Solution 2
//Moores Voting Algorithm
class Solution 
{
    public int majorityElement(int[] nums) 
    {
        int count = 1; 
        int ele = nums[0];
            
        for(int i = 1 ; i<nums.length ; i++)
        {
            if(nums[i]==ele) count++;
            else count--;
            
            if(count == 0)
            {
                ele = nums[i];
                count = 1;
            }
        }
        return ele;
    }
}