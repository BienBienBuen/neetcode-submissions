class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp stuff too
        #max(rob the ith house + res[i-2], don't rob ith house + res[i-1])
        res = [0]*len(nums)
        if len(nums) == 1:
            return nums[0]
            
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            res[i] = max(res[i-2]+nums[i], res[i-1])
        return res[-1]