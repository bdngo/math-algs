from re import search

BAD_LETTERS = '[gkmqvwxz]'
words_list = open("words.txt").read().split('\n')

def longest_word(txt: str, regex: str) -> str:
    """Returns the longest string in TXT excluding REGEX."""
    longest = ''
    for i in txt:
        if len(i) > len(longest) and not search(BAD_LETTERS, i):
            longest = i
    return longest
