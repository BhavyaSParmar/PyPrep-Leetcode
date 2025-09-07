class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(start: int, remain: int):
            if remain == 0:
                res.append(path.copy())
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > remain:   # pruning
                    break
                path.append(c)
                # i (not i+1) because we can reuse the same number
                dfs(i, remain - c)
                path.pop()

        dfs(0, target)
        return res
