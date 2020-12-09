from __future__ import annotations
from typing import Generic, List, TypeVar, Union

T = TypeVar('T') 

class LinkedList(Generic[T]):
    """Class for a linked list."""
    null = None

    def __init__(self, head: T, tail: Union[None, LinkedList]=null):
        assert tail is LinkedList.null or isinstance(tail, LinkedList)
        self.head = head
        self.tail = tail 

    def __repr__(self) -> str:
        if self.tail is not LinkedList.null:
            tail_repr = ', ' + repr(self.tail)
        else:
            tail_repr = ''
        return 'LinkedList(' + repr(self.head) + tail_repr + ')'

    @staticmethod
    def from_list(lst: List[T]) -> LinkedList:
        linked = LinkedList.null
        for i in reversed(lst):
            linked = LinkedList(i, linked)
        return linked

    def to_list(self) -> List[T]:
        lst = []
        while self is not LinkedList.null:
            lst.append(self.head)
            self = self.tail
        return lst

    def prepend(self, node: LinkedList) -> None:
        self = LinkedList(node, self)

    def append(self, node: LinkedList) -> None:
        ptr = self
        while ptr.tail is not LinkedList.null:
            ptr = ptr.tail
        ptr.tail = LinkedList(node)


def main() -> None:
    llst = LinkedList.from_list([1, 2, 3, 4, 5])
    print(llst.to_list())
    llst.append(6)
    llst.prepend(0)
    print(llst.to_list())


if __name__ == "__main__":
    main()
