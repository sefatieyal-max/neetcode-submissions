class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [1] * n
        left = [1] * n
        res = []
        for i in range(1,n):
            right[i] = right[i-1] * nums[i-1]
            left[n-i-1] = left[n-i] * nums[n-i]
        for i in range(n):
            res.append(right[i]*left[i])

        return res
            
        