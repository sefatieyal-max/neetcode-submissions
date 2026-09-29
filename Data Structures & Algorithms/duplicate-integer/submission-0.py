class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        apearence = set()
        for i in nums:
            if i in apearence:
                return True
            else:
                apearence.add(i)
        return False

        