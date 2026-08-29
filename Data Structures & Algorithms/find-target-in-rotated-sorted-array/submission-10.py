class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        m = 0

        #try to locate a length 2 list
        #then try to see where target is
        while l < r-1:
            m = l + (r-l)//2
            if nums[m] > nums[r]: #left is monotone increasing
                if target <= nums[m] and target >= nums[l]:
                    r = m
                else:
                    l = m + 1
            elif nums[m] < nums[r]: #right is monotone increasing
                if target >= nums[m] and target <= nums[r]:
                    l = m
                else:
                    r = m - 1


        if target == nums[l]:
            return l
        elif target == nums[r]:
            return r
        elif target == nums[m]:
            return m
        else:
            return -1