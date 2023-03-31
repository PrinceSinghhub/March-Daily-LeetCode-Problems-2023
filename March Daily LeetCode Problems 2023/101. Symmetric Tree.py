# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isSymmetricorNot(self, left, right):

        if left == None or right == None:
            return left == right

        if left.val != right.val:
            return False

        return self.isSymmetricorNot(left.left, right.right) and self.isSymmetricorNot(left.right, right.left)

    def isSymmetric(self, root):

        if root == None:
            return True
        return self.isSymmetricorNot(root.left, root.right)
