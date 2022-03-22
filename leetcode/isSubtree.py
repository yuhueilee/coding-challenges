'''
Question: Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example:
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

    Input: root = [1,null,1,null,1,null,1,null,1,null,1,2], subRoot = [1,null,1,null,1,null,1,2]
    Output: true
'''
from typing import Optional


class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        """Find whether the subRoot is a subtree of root

        Args:
            root (TreeNode): a node
            subRoot (TreeNode): a node

        Returns:
            bool: whether the subRoot is a subtree of root
        
        Time complexity:
            Best O(N) when all nodes in root has a different value from all nodes in sub root
            Worst O(NM) since at each node we check if the subtree is found or not
            where N is the number of nodes in root and M is the number of nodes in sub root

        Space complexity:
            Best and Worst O(N + M)
            where N is the number of nodes in root and M is the number of nodes in sub root
        """
        res = self.dfs(root, subRoot)
        return res
    
    def dfs(self, root, subRoot) -> bool:
        # Root is None
        if root is None:
            return False
        # Root and subroot have the same value
        if root.val == subRoot.val:
            # Check the left subtrees are identical
            sameLeft = self.dfsTwoTrees(root.left, subRoot.left)
            if sameLeft:
                # Check the right subtrees are identical
                sameRight = self.dfsTwoTrees(root.right, subRoot.right)
                # TERMINATION
                if sameRight:
                    return True
            # Traverse left
            foundLeft = self.dfs(root.left, subRoot)
            if not foundLeft:
                # Traverse right
                foundRight = self.dfs(root.right, subRoot)
                # TERMINATION
                if not foundRight:
                    return False
            # TERMINATION
            return True
        # Root and subroot have the different values
        if root.val != subRoot.val:
            # Traverse left
            foundLeft = self.dfs(root.left, subRoot)
            if not foundLeft:
                # Traverse right
                foundRight = self.dfs(root.right, subRoot)
                # TERMINATION
                if not foundRight:
                    return False
            # TERMINATION
            return True
    
    def dfsTwoTrees(self, curr_one, curr_two) -> bool:
        # Base cases
        if curr_one is None and curr_two is None:
            return True
        if (curr_one is not None and curr_two is None) or (curr_one is None and curr_two is not None):
            return False
        # Same value
        if curr_one.val == curr_two.val:
            sameLeft = self.dfsTwoTrees(curr_one.left, curr_two.left)
            if sameLeft:
                sameRight = self.dfsTwoTrees(curr_one.right, curr_two.right)
                # TERMINATION
                if sameRight:
                    return True
            # TERMINATION
            return False
        # Different values
        elif curr_one.val != curr_two.val:
            # TERMINATION
            return False

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(
  val=1, 
  right=TreeNode(
    val=1, 
    right=TreeNode(
      val=1, 
      right=TreeNode(
        val=1, 
        right=TreeNode(
          val=1, 
          right=TreeNode(
            val=1, 
            left=TreeNode(val=2)
))))))

subRoot = TreeNode(
    val=1, 
    right=TreeNode(
      val=1, 
      right=TreeNode(
        val=1, 
        right=TreeNode(
          val=1, 
          left=TreeNode(val=2)
))))

sol = Solution()
print(sol.isSubtree(root, subRoot))