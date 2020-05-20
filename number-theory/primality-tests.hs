trialDiv :: Integer -> Bool

trialDiv n = all (\x -> n `mod` x /= 0) $ init [2..n]
