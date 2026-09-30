class Solution:

    def encode(self, strs: List[str]) -> str:
        massage = []
        for word in strs:
            massage.append(f"{len(word)}#{word}")
        return "".join(massage)

    def decode(self, s: str) -> List[str]:
        words = []
        end = 0
        while end < len(s):
            start = end
            while s[start] != '#':
                start += 1
            length = int(s[end:start])
            start += 1
            end = start + length
            word = s[start:end]
            words.append(word)
        return words
