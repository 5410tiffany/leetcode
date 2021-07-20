#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


class Solution {
public:
    
    
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int max_so_far[20000]={0};
        int min_so_far[20000]={0};
        int ans = INT_MIN;
   
        for (int i=0;i<n;i++){
            if(i==0){
                max_so_far[i] = nums[i];
                min_so_far[i] = nums[i];
                cout << max_so_far[i] << " " << min_so_far[i] << endl;
            }
            else{
                max_so_far[i] = max({nums[i], nums[i] * max_so_far[i-1], nums[i] * min_so_far[i-1]});
                min_so_far[i] = min({nums[i], nums[i] * max_so_far[i-1], nums[i] * min_so_far[i-1]});
                cout << max_so_far[i] << " " << min_so_far[i] << endl;
            }
            
            ans = (max_so_far[i] > ans ? max_so_far[i] : ans); //update ans to get global max so far
        }
        return ans;
    }
};
