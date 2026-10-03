class Solution:
    def climbStairs(self, n: int) -> int:
        oneStep, twoStep = 1, 1

        for i in range(n-1):
            tmp = oneStep
            oneStep = oneStep + twoStep
            twoStep = tmp
        return oneStep
    
        