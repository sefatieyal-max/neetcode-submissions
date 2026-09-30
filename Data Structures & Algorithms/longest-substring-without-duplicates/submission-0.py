class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 0
        longest = 0
        while left < len(s) and right < len(s):
            if s[right] in seen :
                seen.remove(s[left])
                left += 1
            else:
                longest = max(longest,(right-left+1))
                seen.add(s[right])
                right += 1

        
        return longest
        