class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #log(m) + log(n)
        #locate vert coord, log(n), locate horizontal coord, log(m)
        def binsearch(values: List[int], target: int) -> int:
            l, r = 0, len(values) - 1
            if target > values[r]:
                return r, r+1
            if target < values[l]:
                return None, None

            while r >= l:
                mid = l + (r-l)//2
                if values[mid] > target:
                    r = mid - 1
                elif values[mid] < target:
                    l = mid + 1
                elif values[mid] == target:
                    return mid, mid 

            return r, l

        vert = [ls[0] for ls in matrix]
        l, r = binsearch(vert, target)

        if l is None:
            return False

        if l == r:
            return True
            
        else:
            l, r = binsearch(matrix[l], target)
            if l == r:
                return True
            else:
                return False

