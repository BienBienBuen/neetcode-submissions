class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minsum = 0
        currsum = 0
        maxsum = -float('inf')

        if len(nums) == 1:
            return nums[0]

        for num in nums:
            s = currsum + num
            minsum = min(currsum, minsum)
            maxsum = max(s - minsum, maxsum) 
            currsum = s
            
        return maxsum
