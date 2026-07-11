class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #have three hash tables.
        hash1 = [set() for item in board]
        hash2 = [set() for item in board]
        hash3 = [set() for item in board]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    num = board[i][j]
                    key = 3*(i // 3)+ (j // 3)
                    if (num in hash1[i]) or (num in hash2[j]) or (num in hash3[key]):
                        return False
                    else:
                        hash1[i].add(board[i][j])
                        hash2[j].add(board[i][j])
                        hash3[key].add(board[i][j])
        return True

        