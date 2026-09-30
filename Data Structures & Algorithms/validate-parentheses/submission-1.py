class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        starts = {'(','{','['}
        for c in range(len(s)):
            if s[c] in starts:
                opens.append(s[c])
            elif not bool(opens):
                return False
            else:
                char = opens.pop()
                match s[c]:
                    case '}':
                        if char != '{':
                            return False
                    case ')':
                        if char != '(':
                            return False
                    case ']':
                        if char != '[':
                            return False
        return not bool(opens)
