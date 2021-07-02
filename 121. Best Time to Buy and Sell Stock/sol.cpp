class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minvalue = INT_MAX;
        int maxprofit = 0;
        for(int i=0;i< prices.size();i++){
            if(minvalue > prices[i]){minvalue = prices[i];}
            else if (maxprofit < (prices[i] - minvalue)){maxprofit = prices[i] - minvalue;}
            
        }
        
        return maxprofit;
    }
        
};
