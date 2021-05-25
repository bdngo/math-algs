module NarcissisticNumber (
    isNarcissistic
) where

import Data.Char ( digitToInt )

isNarcissistic :: Integer -> Bool
isNarcissistic n = sum (map (\x -> digitToInt x ^ length s) s) == fromIntegral n
    where s = show n
