module Path (
    findPaths
) where

boardSize :: Integer
boardSize = 8

findPaths :: (Integer, Integer) -> (Integer, Integer) -> Integer
findPaths (startX, startY) (destX, destY)
    | startX == destX && startY == destY = 1
    | startY >= boardSize || startY > destY = 0
    | startX <= 0 = findPaths (startX + 1, startY + 1) (destX, destY)
    | startX >= boardSize = findPaths (startX - 1, startY + 1) (destX, destY)
    | otherwise = findPaths (startX - 1, startY + 1) (destX, destY) + findPaths (startX + 1, startY + 1) (destX, destY)
