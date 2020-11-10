module Elo (
    playerA,
    playerB,
    updateRanking
) where

playerA :: Integer -> Integer -> Double
playerA ra rb = 1 / (1 + 10**(fromIntegral (rb - ra) / diffWeight))
    where diffWeight = 400

playerB :: Integer -> Integer -> Double
playerB ra rb = 1 - playerA ra rb

updateRanking :: Integer -> Double -> Double -> Integer
updateRanking ranking actual expected = ranking + round (kFactor * (actual - expected))
    where kFactor = 32
