import qualified Data.Map as M
import Data.List
import Data.Function
import Data.Maybe

{-- CONSTRUCTOR --}

data HuffmanTree =
    Internal Integer HuffmanTree HuffmanTree | Leaf Char Integer
    deriving (Show)

freq :: HuffmanTree -> Integer
freq (Internal f _ _) = f
freq (Leaf _ f) = f

char :: HuffmanTree -> Char
char (Leaf c _) = c
char (Internal _ _ _) = '-'

{-- ENCODING --} 

construct :: [HuffmanTree] -> HuffmanTree
construct = head . conHelper

conHelper :: [HuffmanTree] -> [HuffmanTree]
conHelper [] = []
conHelper [x] = [x]
conHelper (a:b:xs) = conHelper $ sortBy (compare `on` freq) (newNode : xs)
    where newNode = Internal (freq a + freq b) a b

map2Leaves :: [(Char, Integer)] -> [HuffmanTree]
map2Leaves = map (\(x, y) -> Leaf x y) 

str2Freq :: String -> [(Char, Integer)]
str2Freq = sortBy (compare `on` snd) . map (\x -> (head x, fromIntegral $ length x)) . group . sort

encode :: String -> (String, HuffmanTree)
encode s = (concat $ map (fromMaybe "" . flip M.lookup charMap) s, tree)
    where
        charMap = M.fromList [(i, enHelper tree "" i) | i <- s]
        tree = construct $ map2Leaves $ str2Freq s

enHelper :: HuffmanTree -> String -> Char -> String
enHelper (Internal _ ls rs) code c = enHelper ls (code ++ "0") c ++ enHelper rs (code ++ "1") c
enHelper t code c = if char t == c then code else ""

decode :: String -> HuffmanTree -> String
decode s t = deHelper t "" s t

deHelper :: HuffmanTree -> String -> String -> HuffmanTree -> String
deHelper ogTree s xs (Leaf c _) = deHelper ogTree (s ++ [c]) xs ogTree
deHelper _ s "" _ = s 
deHelper ogTree s (x:xs) (Internal _ ls rs)
    | x == '0' = deHelper ogTree s xs ls
    | otherwise = deHelper ogTree s xs rs

testStr :: String
testStr = "the quick brown fox jumps over the lazy dog"
