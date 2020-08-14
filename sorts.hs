import qualified Data.Map as M

testList :: (Ord a, Integral a) => [a]
testList = [6, 18, 14, 19, 20, 12, 3, 7, 16, 8]

insertionSort :: (Ord a) => [a] -> [a]
insertionSort = isHelper []

isHelper :: (Ord a) => [a] -> [a] -> [a]
isHelper xs [] = xs
isHelper ys (x:xs) = isHelper (is2Helper x ys) xs

is2Helper :: (Ord a) => a -> [a] -> [a]
is2Helper x [] = [x]
is2Helper x (y:ys) = if x <= y then (x:y:ys) else y:is2Helper x ys

-- selectionSort :: (Ord a) => a -> [a] -> [a]
-- selectionSort [] = []
-- selectionSort xs = small : selectionSort $ filter (>=small) xs
--     where small = minimum xs

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = quicksort (filter (<=x) xs) ++ [x] ++ quicksort (filter (>x) xs)

mergesort :: (Ord a) => [a] -> [a]
mergesort [] = []
mergesort [x] = [x]
mergesort xs = merge (mergesort left) (mergesort right)
    where
        half = length xs `div` 2
        left = take half xs
        right = drop half xs

merge :: (Ord a) => [a] -> [a] -> [a]
merge as [] = as
merge [] bs = bs
merge (a:as) (b:bs)
    | a <= b = a : merge as (b:bs)
    | otherwise = b : merge (a:as) bs

emptyRadix :: (Integral a) => M.Map a [a]
emptyRadix = M.fromList [(i, []) | i <- [0..9]]

lsdSort :: (Integral a) => [a] -> [a]
lsdSort = lsdHelper emptyRadix 1

lsdHelper :: (Integral a) => M.Map a [a] -> a -> [a] -> [a]
lsdHelper _ 1000000 xs = xs
lsdHelper radixMap mask [] = lsdHelper emptyRadix (mask * 10) (concat $ M.elems radixMap)
lsdHelper radixMap mask (x:xs) = lsdHelper (M.insertWith (flip (++)) (x `div` mask `mod` 10) [x] radixMap) mask xs
