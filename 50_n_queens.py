class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res: List[List[str]] = []
        all_mask = (1 << n) - 1  

        def backtrack(row: int, cols: int, diag1: int, diag2: int, pos: List[int]) -> None:
            if row == n:
               
                res.append([
                    "." * c + "Q" + "." * (n - c - 1)
                    for c in pos
                ])
                return

            
            free = all_mask & ~(cols | diag1 | diag2)

            while free:
                bit = free & -free             
                free -= bit                   
                col = (bit.bit_length() - 1)   

                pos.append(col)
                
                backtrack(
                    row + 1,
                    cols | bit,
                    (diag1 | bit) << 1 & all_mask, 
                    (diag2 | bit) >> 1,           
                    pos
                )
                pos.pop()

        backtrack(0, 0, 0, 0, [])
        return res
