class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        response = []
        for i in range(0,len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                target = 0 - nums[i]
                left = i + 1
                right = len(nums)-1
                while left < right:
                    sum_num = nums[left] + nums[right]
                    if sum_num == target:
                        response.append([nums[i],nums[left], nums[right]])
                        left += 1
                        while nums[left] == nums[left-1] and left < right:
                            left+= 1
                    elif sum_num < target:
                        left += 1
                    elif sum_num > target:
                        right -= 1
        return response


        