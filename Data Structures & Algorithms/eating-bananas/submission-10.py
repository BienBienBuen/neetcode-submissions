from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper: total hours needed if eating at speed k
        def total_hours(k: int) -> int:
            hours = 0
            for pile in piles:
                # ceil(pile / k)
                hours += (pile + k - 1) // k
            return hours

        # Binary search for minimal k
        left, right = 1, max(piles)   # speed cannot be 0, and > max is never needed

        while left < right:
            mid = (left + right) // 2
            if total_hours(mid) <= h:
                # feasible -> try smaller speed
                right = mid
            else:
                # not feasible -> need larger speed
                left = mid + 1

        return left