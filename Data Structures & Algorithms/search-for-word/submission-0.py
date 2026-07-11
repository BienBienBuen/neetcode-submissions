class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        
        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r, c) in visited or board[r][c] != word[idx]):
                return False
            
            visited.add((r, c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, idx + 1):
                    return True
            visited.remove((r, c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False