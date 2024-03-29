'''
714. Best Time to Buy and Sell Stock with Transaction Fee

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i;
and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

By:shenqiti
2019/8/13
'''

'''
Intuition and Algorithm

At the end of the i-th day, we maintain cash, the maximum profit we could have if we did not have a share of stock, 
and hold, the maximum profit we could have if we owned a share of stock.

To transition from the i-th day to the i+1-th day, we either sell our stock cash = max(cash, hold + prices[i] - fee)
 or buy a stock hold = max(hold, cash - prices[i]). At the end, we want to return cash. 
We can transform cash first without using temporary variables
 because selling and buying on the same day can't be better than just continuing to hold the stock.

'''

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash,hold = 0,-prices[0]
        for i in range(1,len(prices)):
            cash = max(cash,hold+prices[i]-fee)
            hold = max(hold,cash-prices[i])
        return cash
dd = Solution()
prices = [1,3,7,5,10,3]
fee = 3
result = dd.maxProfit(prices,fee)
print(result)
