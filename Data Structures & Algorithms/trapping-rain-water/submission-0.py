class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0 , len(height) - 1
        LBars, RBars = [0] * len(height), [0] * len(height)

        for i in range(1,len(height)-1):
            LBars[l+i] = max(LBars[l+i-1],height[l+i-1])
            RBars[r-i] = max(RBars[r-i+1],height[r-i+1])
        water = 0
        for i in range(len(height)):
            water += max(0,min(LBars[i],RBars[i]) - height[i])

        return water

