class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match_chars = {")":"(","]" : "[", "}" : "{" }
        for c in s:
            if c in match_chars:
                if stack and stack[-1] == match_chars[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
        