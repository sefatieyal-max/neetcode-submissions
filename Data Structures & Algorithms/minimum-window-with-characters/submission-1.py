class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        min_res = len(s)
        l = 0 
        count = {}
        target_map = {}
        for i in range(len(t)):
            target_map[t[i]] = target_map.get(t[i],0) + 1
        need = len(target_map)
        for r in range(len(s)):
            if s[r] in target_map:
                count[s[r]] = count.get(s[r],0) + 1
                if count[s[r]] == target_map[s[r]]:
                    need -= 1
                while need == 0:
                    curr_len = (r-l) + 1
                    if curr_len <= min_res:
                        min_res = curr_len
                        res = s[l:r+1]

                    if s[l] in target_map:
                        count[s[l]] -= 1
                        if count[s[l]] < target_map[s[l]]:
                            need += 1
                    curr_len = r-l

                    l += 1

        return res                