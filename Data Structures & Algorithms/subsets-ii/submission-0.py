class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                      # ensure consistent ordering
        existing_sets = {()}             # start with empty subset
        
        for num in nums:
            new_subsets = []             # collect additions
            for subset in existing_sets:
                new_subsets.append(subset + (num,))
            for new_sub in new_subsets:
                if new_sub not in existing_sets:
                    existing_sets.add(new_sub)
        
        return [list(subset) for subset in existing_sets]