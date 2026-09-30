class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            size = (right-left)*min(heights[left],heights[right])
            largest = max(largest,size)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return largest
            

        