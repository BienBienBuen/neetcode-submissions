class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search? Some variant of binary search
        #i fucking hate binary search....


        # l, l + (r - l) // 2,   r. three points
        """
            
            if a <= b > c, we take [b+1, c]
            if a >= b < c, we take [a, b-1]

            essentially, we want to find the monotone increasing part and not take that part


            consider the case of [1, 2] or [2, 1]

             a = b < c
             a = b > c


        """

        l, r = 0, len(nums)-1

        if r == 0:
            return nums[0]

        while l < r:
            m = l + (r-l)//2
            a, b, c = nums[l], nums[m], nums[r]
            print(str(a)+str(b)+str(c))

            # if (r - l) == 2:
            #     l, r = m, m
            #     break

            if a <= b and b > c:
                l = m + 1
            elif a >= b and b < c:
                r = m 
            elif a < b and b < c:
                r = l
        
        return nums[l]
        #termination happens when l == r


