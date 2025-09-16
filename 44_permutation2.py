class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                   
        n = len(nums)
        used = [False] * n
        ans, path = [], []

        def dfs():
            if len(path) == n:
                ans.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return ans