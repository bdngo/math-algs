module Bisection (
    bisection
) where

bisection :: (Double -> Double) -> (Double, Double) -> Double -> Double
bisection f (lower, upper) threshold
    | abs lBound <= threshold = lower
    | abs uBound <= threshold = upper
    | signum lBound /= signum mBound = bisection f (lower, mid) threshold
    | signum uBound /= signum mBound = bisection f (mid, upper) threshold
    where
        mid = (lower + upper) / 2
        lBound = f lower
        uBound = f upper
        mBound = f mid
