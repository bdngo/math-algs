data BST a = EmptyBST | BST {
    val :: a,
    left :: BST a,
    right :: BST a
} deriving (Show, Eq, Ord)

isLeaf :: (Eq a) => BST a -> Bool
isLeaf t = left t == EmptyBST && right t == EmptyBST

find :: (Ord a) => BST a -> a -> Maybe a
find EmptyBST _ = Nothing
find t x
    | val t == x = Just x
    | x < val t = find (left t) x
    | otherwise = find (right t) x

insert :: (Ord a) => BST a -> a -> BST a
insert EmptyBST x = BST x EmptyBST EmptyBST
insert t x
    | x == val t = t
    | x < val t = BST (val t) (insert (left t) x) (right t)
    | otherwise = BST (val t) (left t) (insert (right t) x)

delete :: (Ord a) => BST a -> a -> BST a
delete EmptyBST _ = EmptyBST
delete t x
    | x < val t = BST (val t) (delete (left t) x) (right t)
    | x > val t = BST (val t) (left t) (delete (right t) x)
    | otherwise = delHelper t

delHelper :: (Ord a) => BST a -> BST a
delHelper t
    | isLeaf t = EmptyBST
    | left t == EmptyBST = right t
    | right t == EmptyBST = left t
    | otherwise = BST (val succNode) (left t) (delete succNode (val succNode))
    where succNode = findSucc (right t)

findSucc :: (Ord a) => BST a -> BST a
findSucc t
    | isLeaf t || left t == EmptyBST = t
    | otherwise = findSucc (left t)

testBST :: BST Integer
testBST = BST 8
            (BST 3
                (BST 1 EmptyBST EmptyBST)
                (BST 6
                    (BST 4 EmptyBST EmptyBST)
                    (BST 7 EmptyBST EmptyBST)))
            (BST 10
                EmptyBST
                (BST 14
                    (BST 13 EmptyBST EmptyBST)
                    EmptyBST))

printBST :: (Show a) => BST a -> [a]
printBST EmptyBST = []
printBST t = printBST (left t) ++ [val t] ++ printBST (right t)
