class BST:
    """A binary search tree."""

    empty = None

    def __init__(self, val, left=empty, right=empty):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return not self.left and not self.right

    def find(self, target):
        if self is BST.empty:
            return "not found"
        if self.val == target:
            return target
        elif target < self.val:
            return BST.find(self.left, target)
        return BST.find(self.right, target)

test_bst = BST(8,
                BST(3,
                    BST(1),
                    BST(6,
                        BST(4),
                        BST(7))
                ),
                BST(10,
                    None,
                    BST(14,
                        BST(13)
                    )
                )
            )
bst = BST(8)
print(bst.find(3))
