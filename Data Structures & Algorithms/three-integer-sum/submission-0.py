class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #check all pairs, see of complement is in dict
        #try something recursive? for each number, 
        #find its complement, run the two sum program
        #on the remaining list(popped)
        #have a result list to append if check is true.
        #For two sum, again use the complement idea, iterate 
        #it item by item for fastest time
        seen = set()
        output = []


        for i in range(len(nums)):

            complement = -nums[i]
            temp_nums = nums[:i] + nums[i+1:]
            sublist = self.twoSum(temp_nums, complement)
            if len(sublist) > 0:
                for item in sublist:
                    item.append(nums[i])
                    subset = frozenset(item)
                    if subset not in seen:
                        output.append(item)
                        seen.add(subset)
        return output 

                
                
    
    def twoSum(self, nums: List[int], target) -> List[List[int]]:
        
        numSet = set()
        output = []
        for num in nums:
            if (target - num) in numSet:
                output.append([target - num, num])
            else:
                numSet.add(num)
        return output

