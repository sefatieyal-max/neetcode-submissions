class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r,l = len(numbers)-1 , 0
        while (l < r):
            curr = numbers[r] + numbers[l]
            if curr == target:
                return [l+1,r+1]
            elif curr < target:
                l += 1
            elif curr > target:
                r -= 1
            
        