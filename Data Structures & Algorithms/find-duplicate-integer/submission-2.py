class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        newlist = [0]*(len(nums)-1)
        for num in nums:
            if newlist[num-1] == 0:
                newlist[num-1]+=1
            else:
                return num 