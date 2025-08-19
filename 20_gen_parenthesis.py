class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s: str, open_used: int, close_used: int) -> None:
            if len(s) == 2 * n:
                res.append(s)
                return
            if open_used < n:                 
                backtrack(s + "(", open_used + 1, close_used)
            if close_used < open_used:         
                backtrack(s + ")", open_used, close_used + 1)

        backtrack("", 0, 0)
        return res
