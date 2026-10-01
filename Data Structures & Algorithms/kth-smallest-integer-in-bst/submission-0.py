# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def size(self, root):
        if not root:
            return 0
        else:
            return 1 + self.size(root.left) + self.size(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node = root
        sizeL = 0
        if node:
            while k > 0:
                sizeL = 1 + self.size(node.left)
                if k == sizeL:
                    k = k - sizeL
                elif k > sizeL:
                    k = k - sizeL
                    node = node.right
                else:
                    node = node.left
        return node.val