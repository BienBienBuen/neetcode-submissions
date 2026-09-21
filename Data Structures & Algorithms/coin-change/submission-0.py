class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #hardest are probably graph related, two pointer, loop detection
        #variations of dfs and bfs
        if amount == 0:
            return 0

        arr = [float('inf') for i in range(amount + 1)]

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin > 0:
                    arr[i] = min(arr[i], 1 + arr[i - coin])
                elif i - coin == 0:
                    arr[i] = 1
        
        if arr[amount] == float('inf'):
            return -1
        else:
            return arr[amount]