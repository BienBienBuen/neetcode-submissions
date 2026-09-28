class Solution:
    def pacificAtlantic(self, heights):
        R, C = len(heights), len(heights[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (0 <= nr < R and 0 <= nc < C 
                    and (nr, nc) not in visited 
                    and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)
        
        pac, atl = set(), set()
        for r in range(R):
            dfs(r, 0, pac)      # left edge
            dfs(r, C-1, atl)    # right edge
        for c in range(C):
            dfs(0, c, pac)      # top edge
            dfs(R-1, c, atl)    # bottom edge
        
        return [list(cell) for cell in pac & atl]