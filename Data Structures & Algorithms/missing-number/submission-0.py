class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = (0 + len(nums))*(len(nums)+1)/2
        numsSum = sum(nums)

        return int(target - numsSum)



        
        