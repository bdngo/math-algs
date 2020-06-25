class BST:
    """A binary search tree."""

    empty = None
    def __init__(self, val, left=empty, right=empty):
        self.val = val
        self.left = left
        self.right = right


    def __str__(self):
        if self is BST.empty:
            return ""
        return BST.__str__(self.left) + " {0} ".format(self.val) + BST.__str__(self.right)


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
    

    def insert(self, node):
        def insert_helper(t, node):
            if t is BST.empty:
                return BST(node)
            if node < t.val:
                t.left = insert_helper(t.left, node)
            elif node > t.val:
                t.right = insert_helper(t.right, node)
            return t
        self = insert_helper(self, node)


    def delete(self, node):
        def find_succ(t):
            curr_succ = t
            while t.left is not BST.empty:
                curr_succ = t.left
            return curr_succ
        if self is BST.empty:
            return
        if node < self.val:
            BST.delete(self.left, node)
        elif node > self.val:
            BST.delete(self.right, node)
        else:
            if not (self.left is BST.empty or self.right is BST.empty):
                successor = find_succ(self)
                self.val = successor.val
                successor.delete(successor.val)
            elif self.left is not BST.empty:
                self = self.left
            elif self.right is not BST.empty:
                self = self.right
            else:
                self = BST.empty


test_bst = BST(8,
                BST(3,
                    BST(1),
                    BST(6,
                        BST(4),
                        BST(7))),
                BST(10,
                    None,
                    BST(14,
                        BST(13))))
print(test_bst)

test_bst.insert(9)
print(test_bst)

test_bst.delete(9)
print(test_bst)
print(test_bst.find(9))
