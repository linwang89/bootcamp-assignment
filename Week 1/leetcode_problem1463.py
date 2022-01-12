# Cherry pickup II
# Dynamic programming
# https://leetcode.com/problems/cherry-pickup-ii/


class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[], []]
        dp[0] = [[0 for _ in grid[0]] for _ in grid[0]]
        dp[1] = [[0 for _ in grid[0]] for _ in grid[0]]

        for j in range(len(grid[0])):
            for k in range(len(grid[0])):
                if j == k:
                    max_cherry = grid[-1][j]
                else:
                    max_cherry = grid[-1][j] + grid[-1][k]
                dp[0][j][k] = max_cherry

        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                for k in range(len(grid[0])):
                    if j == k:
                        max_cherry = grid[-1 - i][j]
                    else:
                        max_cherry = grid[-1 - i][j] + grid[-1 - i][k]
                    tmp = 0
                    for m in [j - 1, j, j + 1]:
                        for n in [k - 1, k, k + 1]:
                            if m >= 0 and m < len(grid[0]) and n >= 0 and n < len(grid[0]):
                                if tmp < dp[0][m][n]:
                                    tmp = dp[0][m][n]
                    dp[1][j][k] = tmp + max_cherry
            dp[0] = [list(x) for x in dp[1]]
        return dp[0][0][-1]
