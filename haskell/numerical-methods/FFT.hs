module FFT (
    fft,
    ifft,
    polyMul
) where

import Data.Function (on)
import Data.Complex (mkPolar, Complex(..), realPart, magnitude)
import Control.Monad (ap)

type CD = Complex Double

split :: [a] -> ([a], [a])
split [] = ([], [])
split [x] = ([x], [])
split (x:y:xs) = (x:xp, y:yp) where (xp, yp) = split xs

evalPoly :: CD -> CD -> CD -> Int -> CD
evalPoly w e o n = e + w^n * o

fft :: [Double] -> [CD]
fft [] = []
fft [x] = [x :+ 0]
fft xs = zipWith3 (evalPoly w) (fftE ++ fftE) (fftO ++ fftO) [0..length xs-1]
    where
        (es, os) = split xs
        (fftE, fftO) = (fft es, fft os)
        w = mkPolar 1 (2 * pi / fromIntegral (length xs))

ifft :: [Complex Double] -> [Double]
ifft = ap (map . (. realPart) . (*) . recip . fromIntegral . length) ifftHelper

ifftHelper :: [CD] -> [CD]
ifftHelper [] = []
ifftHelper [x] = [x]
ifftHelper xs = zipWith3 (evalPoly w) (ifftE ++ ifftE) (ifftO ++ ifftO) [0..length xs-1]
    where
        (es, os) = split xs
        (ifftE, ifftO) = (ifftHelper es, ifftHelper os)
        w = mkPolar 1 (-2 * pi / fromIntegral (length xs))

polyMul :: [Double] -> [Double] -> [Double]
polyMul p1 p2 = ifft ((zipWith (*) `on` (fft . pad)) p1 p2)
    where pad xs = xs ++ replicate (length xs) 0
