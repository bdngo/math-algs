import System.Random

estimatePi :: Integer -> Double
estimatePi sims = 4 * (piHelper 0 sims (mkStdGen 100)) / (fromIntegral sims)

piHelper :: Double -> Integer -> StdGen -> Double
piHelper est 0 _ = est
piHelper est sims gen = piHelper newEst (sims - 1) newGen
    where
        newEst = if x * x + y * y <= 1 then est + 1 else est
        (x, gen1) = randomR (-1, 1) gen :: (Double, StdGen)
        (y, newGen) = randomR (-1, 1) gen1 :: (Double, StdGen)

monteCarloInt :: (Double -> Double) -> (Double, Double) -> Integer -> Double
monteCarloInt f (left, right) sims = deltaX * mciHelper f (left, right) sims 0 (mkStdGen 100)
    where deltaX = (right - left) / (fromIntegral sims)

mciHelper :: (Double -> Double) -> (Double, Double) -> Integer -> Double -> StdGen -> Double
mciHelper _ (_, _) 0 est _ = est
mciHelper f (left, right) sims est gen = mciHelper f (left, right) (sims - 1) (est + integral) newGen
    where
        integral = f x
        (x, newGen) = randomR (left, right) gen :: (Double, StdGen)
