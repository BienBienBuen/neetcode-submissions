class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        if not nums or len(nums) == 0:
            return -1
        
        if target > nums[mid]:
            relative_idx = self.search(nums[mid+1:], target)
            return -1 if relative_idx == -1 else relative_idx + (mid + 1)
        elif target < nums[mid]:
            return self.search(nums[:mid], target)
        elif target == nums[mid]:
            return mid