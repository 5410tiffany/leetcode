#include<algorithm>
#include<vector>

class Solution {
public:
    int rob(vector<int>& nums) {
        int rob[101] ={0};
        for (int i=0;i<nums.size();i++){
            
            if(i==0){rob[i] = nums[i];}
            else if(i==1){rob[i] = max(nums[i], rob[i-1]);}
            
            else{
                rob[i] = max(nums[i] + rob[i-2], rob[i-1]);
            }
        }
        return rob[nums.size()-1];
    }
};
