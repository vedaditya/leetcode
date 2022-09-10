class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        @cache
        def dfs(ind: int, can_sell: bool, k: int):
            if k == 0: return 0
            if ind == N: return 0

            if ind == N - 1: 
                if can_sell:
                    return prices[ind]
                else:
                    return 0

            if can_sell:
                res = max(dfs(ind + 1, True, k), prices[ind] + dfs(ind + 1, False, k - 1))
            else:
                res = max(dfs(ind + 1, False, k), -prices[ind] + dfs(ind + 1, True, k))

            return res

        return dfs(0, False, k)