import Data.List

primeFactors :: Integer -> [Integer]
pfHelper :: Integer -> Integer -> [Integer]
printPF :: [Integer] -> [(Integer, Int)]
factorize :: Integer -> [Integer]
isPerfectNum :: Integer -> Bool

primeFactors n = pfHelper n 2

pfHelper 1 _ = []
pfHelper n k
    | n `mod` k == 0 = k : pfHelper (n `div` k) k
    | otherwise = pfHelper n (k + 1)

printPF xs = map (\x -> (head x, length x)) $ group xs

factorize n = filter (\x -> n `mod` x == 0) [1..n]

isPerfectNum n = (sum $ init $ factorize n) == n
