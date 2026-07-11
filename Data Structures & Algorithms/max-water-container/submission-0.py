class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #use pointers?
        h = 0
        l = 0
        r = len(heights)-1
        maxvol = 0
        #we go from two sides inwards
        #go by height. for each height, we look for
        #widest possible base

        while l < r:
            while heights[l] < h and l < r:
                l+=1
            
            while heights[r] < h and l < r:
                r-=1
            
            vol = min(heights[l], heights[r]) * (r-l)
            if vol > maxvol:
                maxvol = vol
            h+=1
        return maxvol



