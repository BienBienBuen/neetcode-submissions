class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #do a dp essentially. a = a(down)+a(right)
        dp = [[0]*(n+1) for i in range(m+1)]
        dp[m-1][n-2] = 1
        dp[m-2][n-1] = 1
        dp[m-1][n-1] = 1

        for i in range(m):
            for j in range(n):
                i_new = m-1-i
                j_new = n-1-j

                if dp[i_new][j_new] == 0:
                    dp[i_new][j_new] = dp[i_new+1][j_new] + dp[i_new][j_new+1]
    
        return dp[0][0]
