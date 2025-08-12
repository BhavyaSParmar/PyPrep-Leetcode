class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            # Skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Optional pruning
            if nums[i] > 0:
                break  # since array is sorted, no three numbers can sum to 0

            l, r = i + 1, n - 1
            target = -nums[i]

            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])

                    # Move both pointers past duplicates
                    l_val, r_val = nums[l], nums[r]
                    while l < r and nums[l] == l_val:
                        l += 1
                    while l < r and nums[r] == r_val:
                        r -= 1

                elif s < target:
                    l += 1
                else:
                    r -= 1

        return res