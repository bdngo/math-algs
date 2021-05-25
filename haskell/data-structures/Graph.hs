module Graph (
    Graph,
    dfs,
    bfs
) where

data Graph a = Graph {
    val :: a,
    nodes :: [Graph a]
} deriving (Show, Eq)

dfs :: (Eq a) => Graph a -> Graph a -> [Graph a]
dfs g v = dfsHelper [v] [] g v

dfsHelper :: (Eq a) => [Graph a] -> [Graph a] -> Graph a -> Graph a -> [Graph a]
dfsHelper [] m _ _ = m
dfsHelper f m g s = dfsHelper
                        (childs ++ tail f)
                        (if curr `elem` m then m else curr:m) g s
    where
        curr = head f
        childs = filter (`elem` m) $ nodes s

bfs :: (Eq a) => Graph a -> Graph a -> [Graph a]
bfs g v = bfsHelper [v] [] g v

bfsHelper :: (Eq a) => [Graph a] -> [Graph a] -> Graph a -> Graph a -> [Graph a]
bfsHelper [] m _ _ = m
bfsHelper f m g s = bfsHelper
                        (tail f ++ childs)
                        (if curr `elem` m then m else curr:m) g s
    where
        curr = head f
        childs = filter (`elem` m) $ nodes s
