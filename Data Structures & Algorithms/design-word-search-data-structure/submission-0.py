
class TreeNode():
    def __init__(self):
        self.sons = {}
        self.end = False
    
class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.sons:
                node.sons[c] = TreeNode()
            node = node.sons[c]
        node.end = True


    def search(self, word: str) -> bool:
        return self.dfs(0, word, self.root)

    def dfs(self, i , word, node):
        for i in range(i,len(word)):
            c = word[i]
            if c == ".":
                for child in node.sons.values():
                    if self.dfs(i+1,word,child):
                        return True
                
                return False
            else:
                if c not in node.sons:
                    return False
                node = node.sons[c]
        return node.end



