trialDiv :: Integer -> Bool

trialDiv n = all (\x -> n `mod` x /= 0) $ [2..round $ sqrt $ fromIntegral n]
