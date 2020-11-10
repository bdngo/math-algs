module LinkedList (
    LinkedList(..),
    fromList,
    toList,
    printLL,
    append,
    prepend
) where

data LinkedList a = EmptyLL | LinkedList {
    headLL :: a,
    tailLL :: LinkedList a
} deriving (Show)

fromList :: [a] -> LinkedList a
fromList = foldr LinkedList EmptyLL

toList :: LinkedList a -> [a]
toList EmptyLL = []
toList lst = headLL lst : toList (tailLL lst)

printLL :: (Show a) => LinkedList a -> String
printLL EmptyLL = "NULL" 
printLL lst = show (headLL lst) ++ " " ++ printLL (tailLL lst)

append :: a -> LinkedList a -> LinkedList a
append x EmptyLL = LinkedList x EmptyLL
append x lst  = LinkedList (headLL lst) (append x (tailLL lst))

prepend :: a -> LinkedList a -> LinkedList a
prepend = LinkedList
