# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildATree(self, inorder, inStart, inEnd, postorder, posStart, posEnd, hasmap):

        if posStart > posEnd or inStart > inEnd:
            return None

        root = TreeNode(postorder[posEnd])

        # finding the index of that rootNode in Inorder
        RootIndex = hasmap[root.val]

        # find the len of remaing leftNode
        NumberOfLeftNode = RootIndex - inStart

        root.left = self.buildATree(inorder, inStart, RootIndex - 1, postorder, posStart,
                                    posStart + NumberOfLeftNode - 1, hasmap)
        root.right = self.buildATree(inorder, RootIndex + 1, inEnd, postorder, posStart + NumberOfLeftNode, posEnd - 1,
                                     hasmap)

        return root

    def buildTree(self, inorder, postorder):

        if inorder == None or postorder == None or len(postorder) != len(inorder):
            return None

        # for provideing the index for which node are root node and which node are child node
        hasmap = {}
        for i in range(len(inorder)):
            hasmap[inorder[i]] = i

        print(hasmap)

        rootNode = self.buildATree(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, hasmap)

        return rootNode


# todo another method

class Solution:
    def buildTree(self, inorder, postorder):
        if inorder:
            IndexofRootNode = inorder.index(postorder.pop())
            root = TreeNode(inorder[IndexofRootNode])
            root.right = self.buildTree(inorder[IndexofRootNode + 1:], postorder)
            root.left = self.buildTree(inorder[0:IndexofRootNode], postorder)
            return root
