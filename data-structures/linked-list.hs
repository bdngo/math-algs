data LinkedList a = EmptyLL | LinkedList {
    headLL :: a,
    tailLL :: LinkedList a
} deriving (Show)

fromList :: [a] -> LinkedList a
fromList [] = EmptyLL
fromList (x:xs) = LinkedList x (fromList xs)

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
