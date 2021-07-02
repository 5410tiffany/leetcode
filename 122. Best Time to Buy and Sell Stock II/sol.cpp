class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int curmin = 0;
        int curprofit = 0;
        int profit = 0;
        prices.insert(prices.begin(), 0);
        
        for(int i = 1; i< prices.size();i++){
            
            if(prices[i] > prices[i-1]){//價格下跌；出場結算
                curprofit = prices[i]-curmin;
            }
            else{//價格下跌；出場結算
                curmin = prices[i];
                profit +=curprofit;
                curprofit = 0;
            }
            cout << curmin << " " << curprofit << endl;
            
        }
        profit +=curprofit;//last day強制結算
            
        return profit - prices[1];
    }
};
