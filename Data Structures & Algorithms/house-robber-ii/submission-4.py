class Solution:
    def robHelper(self, nums):
        rob1, rob2 = 0, 0
    
        for n in nums:
        
            tmp = max(n + rob1 ,rob2)
            rob1 = rob2
            rob2 = tmp

        return rob2

    def rob(self, nums: List[int]) -> int:

        
        return max(nums[0],self.robHelper(nums[1:]),self.robHelper(nums[:-1]))
    

        