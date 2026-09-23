class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
    
        #actually, we just need to rotate the coordinates?
        # 0 1
        # -1 0
        x, y = len(matrix), len(matrix[0])
        #coord_matrix = [[(i, j) for i in range(y)] for j in range(x)]
        #output_matrix = [[0]*y for _ in range(x)]
        rotated = set()

        def rot(coord, val):
            if coord in rotated:
                pass
                
            else:
                a, b = coord
                anew, bnew = b, x-1-a
                rotated.add((a, b))

                if (anew, bnew) in rotated:
                    #this means this coord value can be safely replaced
                    matrix[anew][bnew] = val
                else:
                    #we recursively rotate away anew, bnew to its new value
                    hold_val = matrix[anew][bnew]
                    matrix[anew][bnew] = val
                    rot((anew, bnew), hold_val)            


        for i in range(x):
            for j in range(y):
                val = matrix[i][j]
                rot((i, j), val)


        return None


    # def matmul(self, A: List[List[int]], B: List[List[int]]) -> int:
    #     xa, ya = len(A), len(A[0])
    #     xb, yb = len(B), len(B[0])

    #     if ya != xb:
    #         return None

    #     output = [[0]*yb for i in range(xa)]
    #     #xa rows, yb columns

    #     for i in range(xa):
    #         for j in range(yb):

