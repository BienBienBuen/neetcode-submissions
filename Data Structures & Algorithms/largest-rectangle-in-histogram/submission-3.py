from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        stack = []          # will store indices of increasing heights
        maxA = 0
        n = len(heights)
        
        for i, h in enumerate(heights):
            # While current height is smaller than the height at stack top
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                # Width = i if stack empty, else i - stack[-1] - 1
                width = i if not stack else i - stack[-1] - 1
                maxA = max(maxA, height * width)
            stack.append(i)
        
        # Process remaining bars in stack (end of array is the right boundary)
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            maxA = max(maxA, height * width)
        
        return maxA