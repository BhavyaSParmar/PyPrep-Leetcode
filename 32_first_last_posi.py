class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(a: List[int], x: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def upper_bound(a: List[int], x: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        left = lower_bound(nums, target)
        if left == len(nums) or (left < len(nums) and nums[left] != target):
            return [-1, -1]

        right = upper_bound(nums, target) - 1
        return [left, right]