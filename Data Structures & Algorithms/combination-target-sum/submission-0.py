from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # dp[s] stores all combinations that sum to s, each combination is sorted
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]                     # base case: empty combination

        # Process numbers in increasing order to ensure combinations are built
        # in non‑decreasing order, which prevents duplicates.
        for num in sorted(nums):
            # For each sum >= num, extend previous combinations
            for s in range(num, target + 1):
                for comb in dp[s - num]:
                    dp[s].append(comb + [num])

        return dp[target]       