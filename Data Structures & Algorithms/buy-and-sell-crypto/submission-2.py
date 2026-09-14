class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = []
        sol.append([prices[0], prices[0], prices[0]])
        # [max_uu, h, ll]
        max_uu = 0
        for i in range(1, len(prices)):
            l, h, ll = sol[i-1][0], sol[i-1][1], sol[i-1][2]
            if prices[i] > h:
                h = prices[i]
            elif prices[i] < ll:
                ll = prices[i]

            if max_uu < max((h-l), (prices[i] - ll)):
                if (h-l) < (prices[i] - ll):
                    max_uu = prices[i] - ll
                    h = prices[i]
                    l = ll
                else:
                    max_uu = h - l
            
            sol.append([l, h, ll])
        return max_uu

        