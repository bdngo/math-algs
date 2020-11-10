module Primality (
    trialDiv,
    lucasLehmerTest
) where

trialDiv :: Integer -> Bool
trialDiv n = all (\x -> n `mod` x /= 0) [2..round $ sqrt $ fromIntegral n]

lucasLehmer :: [Integer]
lucasLehmer = 4 : map (\x -> x^2 - 2 :: Integer) lucasLehmer

lucasLehmerTest :: Integer -> Bool
lucasLehmerTest n
    | n < 2 || not (trialDiv n) = False
    | otherwise = (lucasLehmer !! max 0 (fromIntegral (n - 2))) `mod` (2^n - 1) == 0
