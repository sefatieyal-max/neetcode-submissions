class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = defaultdict(int)
        for i,j in zip(s,t):
            letters[i] += 1
            letters[j] -= 1 
        for count in letters.values():
            if count != 0:
                return False
        return True

        