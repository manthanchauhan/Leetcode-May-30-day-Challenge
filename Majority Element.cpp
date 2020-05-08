class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int,int> mp;
        
        for(int i=0;i<nums.size();i++)
            mp[nums[i]]++;
        
        int n = nums.size();
       
        for(int i=0;i<nums.size();i++){
            if(mp[nums[i]] > n/2)
                return nums[i];
       
        }
        
        return 0;
    }
};

//Another way is to use Moore's Voting Algorithm
