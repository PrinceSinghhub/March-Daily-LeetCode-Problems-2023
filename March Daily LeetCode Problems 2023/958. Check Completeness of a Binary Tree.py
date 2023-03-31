# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def numberOfNodes(self, root):

        if root == None:
            return 0

        ans = 1 + self.numberOfNodes(root.left) + self.numberOfNodes(root.right)

        return ans

    def chekBalancedTree(self, root, index, cout):

        if root == None:
            return True

        if index >= cout:
            return False


        else:

            left = self.chekBalancedTree(root.left, 2 * index + 1, cout)
            right = self.chekBalancedTree(root.right, 2 * index + 2, cout)

            return left & right

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        cout = self.numberOfNodes(root)
        return self.chekBalancedTree(root, 0, cout)
