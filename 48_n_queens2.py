class Solution:
    def totalNQueens(self, n: int) -> int:
        ALL = (1 << n) - 1 

        def dfs(cols: int, diag: int, anti: int) -> int:
          
            if cols == ALL:
                return 1  
            count = 0
           
            free = ALL & ~(cols | diag | anti)

            while free:
                bit = free & -free       
                free -= bit               
                
                count += dfs(cols | bit, (diag | bit) << 1 & ALL, (anti | bit) >> 1)
            return count

        return dfs(0, 0, 0)
