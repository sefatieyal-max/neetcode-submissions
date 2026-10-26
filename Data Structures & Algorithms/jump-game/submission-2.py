class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums)-1] = True
        for i in range(len(nums)-2,-1,-1):
            for jump in range(nums[i],0,-1):
                if i + jump < len(nums):
                    dp[i] = dp[i] or dp[i+jump]

        return dp[0]
