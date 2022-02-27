class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        p1 = 0
        p2 = 1
        p3 = 2
        not_found = True
        while not_found and p3 < n:
            if nums[p1] + nums[p2] > nums[p3] and nums[p1] + nums[p3] > nums[p2] and nums[p3] + nums[p2] > nums[p1]:
                return nums[p1] + nums[p2] + nums[p3]
            p3 += 1
            if p3 == n and n > 3:
                p1 += 1
                p2 = p1 + 1
                p3 = p2 + 1

        return 0