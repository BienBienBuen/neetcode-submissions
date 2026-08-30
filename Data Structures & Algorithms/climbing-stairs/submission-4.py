class Solution:
    def climbStairs(self, n: int) -> int:
        results = [0]*n
        if n >= 2:
            results[0], results[1] = 1,2
        elif n == 1:
            return 1
        
        for i in range(2, len(results)):
            results[i] = results[i-1] + results[i-2]
        return results[-1]