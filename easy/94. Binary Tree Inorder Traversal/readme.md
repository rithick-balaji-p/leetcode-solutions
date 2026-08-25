# Binary Tree Inorder Traversal

## Problem

Given the root of a binary tree, return the inorder traversal of its nodes' values.

**Inorder Traversal:**
`Left → Root → Right`

## Approach

We use **recursion** to traverse the binary tree.

1. Traverse the left subtree.
2. Visit the current node.
3. Traverse the right subtree.

## Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        # If the tree is empty, return an empty list
        if not root:
            return []

        # List to store the inorder traversal
        traversal = []

        # Recursive function for inorder traversal
        def inorder(root):

            # Traverse the left subtree
            if root.left:
                inorder(root.left)

            # Visit the current node
            traversal.append(root.val)

            # Traverse the right subtree
            if root.right:
                inorder(root.right)

        # Start traversal from the root
        inorder(root)

        # Return the inorder traversal
        return traversal
```

## Example

For the binary tree:

```text
        1
         \
          2
         /
        3
```

**Output:**

```text
[1, 3, 2]
```

## Concepts Used

* Binary Tree
* Inorder Traversal
* Recursion
* Depth First Search (DFS)

## Complexity Analysis

### Time Complexity

**O(n)**

Each node is visited exactly once.

### Space Complexity

**O(h)**

 where `h` is the height of the tree.


## Key Point

**Inorder Traversal = Left → Root → Right**

For a **Binary Search Tree (BST)**, inorder traversal gives the elements in **sorted order**.
