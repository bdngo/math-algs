from __future__ import annotations
from typing import Generic, TypeVar, Union

T = TypeVar('T') 

class BST(Generic[T]):
    """A binary search tree."""

    empty = None
    def __init__(self, val: T,
                    left: Union[None, BST]=empty,
                    right: Union[None, BST]=empty):
        self.val = val
        self.left = left
        self.right = right


    def __str__(self) -> str:
        if self is BST.empty:
            return ""
        return BST.__str__(self.left) + " {0} ".format(self.val) + BST.__str__(self.right)


    def is_leaf(self) -> bool:
        return not self.left and not self.right


    def find(self, target: T) -> Union[str, T]:
        if self is BST.empty:
            return "not found"
        if self.val == target:
            return target
        elif target < self.val:
            return BST.find(self.left, target)
        return BST.find(self.right, target)


    def insert(self, node: BST) -> None:
        def insert_helper(t: BST, node: BST) -> BST:
            if t is BST.empty:
                return BST(node)
            if node < t.val:
                t.left = insert_helper(t.left, node)
            elif node > t.val:
                t.right = insert_helper(t.right, node)
            return t
        self = insert_helper(self, node)


    def delete(self, node: BST) -> None:
        def find_succ(t: BST) -> BST:
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


    def is_BST(self):
        if self == BST.empty or self.is_leaf():
            return True
        if self.left == BST.empty:
            return self.val < self.right.val and self.right.is_BST()
        elif self.right == BST.empty:
            return self.left.is_BST and self.val > self.left.val
        return self.left.is_BST and self.left.val < self.val < self.right.val and self.right.is_BST()


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
