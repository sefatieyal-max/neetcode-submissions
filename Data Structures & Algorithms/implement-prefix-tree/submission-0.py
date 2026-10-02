class TreeNode:
    def __init__(self):
        self.sons = {}
        self.endWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.sons:
                node.sons[c] = TreeNode()
            node = node.sons[c]
        node.endWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.sons:
                return False
            node = node.sons[c]
        return node.endWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.sons:
                return False
            node = node.sons[c]
        return True
        
        