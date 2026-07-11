class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numDict = {}
        for i in range(len(nums)):
            numDict[nums[i]] = i


        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in numDict and (numDict[diff] != i):
                return [i, numDict[diff]]

        