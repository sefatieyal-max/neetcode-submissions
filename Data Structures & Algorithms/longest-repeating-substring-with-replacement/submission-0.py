class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0 
        max_freq = 0
        for r in range(len(s)):
            curr_freq = 1 + count.get(s[r],0)
            count[s[r]] = curr_freq
            max_freq = max(max_freq, curr_freq)
            while (r-l+1) - max_freq > k:
                count[s[l]] = count.get(s[l]) -1
                l += 1
            res = max(res, r-l+1)
        return res

                

        