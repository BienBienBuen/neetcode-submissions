class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #dynamic programming. Iteratively generate solution.
        if len(nums) == 0:
            return [[]]
        elif len(nums) == 1:
            return [[], nums]
        else:
            prev_subsets = self.subsets(nums[:-1])
            output = prev_subsets.copy()
            last_element = nums[-1]
            print(output)
            for subset in prev_subsets:
                new_sub = subset.copy()
                new_sub.append(last_element)
                output.append(new_sub)
            return output