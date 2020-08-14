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

-- TODO: LSD sort
-- lsdSort :: (Ord a) => [a] -> [a]
