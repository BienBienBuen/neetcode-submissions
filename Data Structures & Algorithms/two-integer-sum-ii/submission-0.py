class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        sol = False
        p1 = 0
        p2 = len(numbers) - 1
        while sol == 0:
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
            else:
                sol = True
                return [p1+1, p2+1]