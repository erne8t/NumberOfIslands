class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0 or len(grid[0])==0: return 0
        # first, add a circumference of '0's
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    self.dfs(i,j,grid)
                    res += 1
        return res

    def dfs(self,i,j,grid):
        grid[i][j] = "0"

        if i+1<len(grid) and grid[i+1][j]=="1": self.dfs(i+1,j,grid)
        if j+1<len(grid[0]) and grid[i][j+1]=="1": self.dfs(i,j+1,grid)
        if i-1>=0 and grid[i-1][j]=="1": self.dfs(i-1,j,grid)
        if j-1>=0 and grid[i][j-1]=="1": self.dfs(i,j-1,grid)
        
