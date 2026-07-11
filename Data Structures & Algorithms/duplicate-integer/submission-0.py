class Solution:


    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashmap? two pointer?
        numDict = {}
        for num in nums:
            if numDict.get(num):
                return True
            else:
                numDict[num] = 1
        return False

        