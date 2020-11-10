module Factors (
    primeFactors,
    printPF,
    factorize,
    isPerfectNum
) where

import Data.List ( group )

primeFactors :: Integer -> [Integer]
primeFactors n = pfHelper n 2

pfHelper :: Integer -> Integer -> [Integer]
pfHelper 1 _ = []
pfHelper n k
    | n `mod` k == 0 = k : pfHelper (n `div` k) k
    | otherwise = pfHelper n (k + 1)

printPF :: [Integer] -> [(Integer, Int)]
printPF xs = map (\x -> (head x, length x)) $ group xs

factorize :: Integer -> [Integer]
factorize n = filter (\x -> n `mod` x == 0) [1..n]

isPerfectNum :: Integer -> Bool
isPerfectNum n = sum (init $ factorize n) == n
