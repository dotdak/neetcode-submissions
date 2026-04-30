class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        def calc_profit(current_weight, i):
            state = (current_weight, i)
            if state in memo: return memo[state]
            if i == len(profit):
                return 0
            
            # Option 1: Skip current item
            res = calc_profit(current_weight, i + 1)
            
            # Option 2: Include current item (if it fits)
            if current_weight + weight[i] <= capacity:
                res = max(res, profit[i] + calc_profit(current_weight + weight[i], i + 1))
            
            memo[state] = res
            return res

        return calc_profit(0, 0)