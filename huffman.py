class HuffmanTree:
    """Class for a node of a Huffman encoding tree."""

    def __init__(self, char, freq=0, left=None, right=None):
        self._char = char
        self._freq = freq
        self._left, self._right = left, right

    def __repr__(self):
        return "'{0}' ({1})\nleft: {2}\nright: {3}\n".format(self._char, self._freq, self._left, self._right)

    @staticmethod
    def construct(nodes):
        while len(nodes) != 1:
            pop1, pop2 = nodes.pop(0), nodes.pop(0)
            new_node = HuffmanTree('', pop1._freq + pop2._freq, pop1, pop2)
            nodes.append(new_node)
            nodes.sort(key=lambda x: x._freq)
        return nodes[0]

    def is_leaf(self):
        return self._left is None and self._right is None


def encode(s):
    def str_to_leaves(s): 
        """Converts S to a dictionary mapping of character frequencies."""
        d = {}
        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1
        f = lambda x: HuffmanTree(x[0], x[1])
        return sorted(map(f, d.items()), key=lambda x: x._freq)
    def encode_helper(c, t, code):
        if t is None or (t._char != c and t._char != ''):
            return ''
        elif t._char == c:
            return code
        return encode_helper(c, t._left, code + '0') + encode_helper(c, t._right, code + '1')
    tree = HuffmanTree.construct(str_to_leaves(s))
    char_map = {i: encode_helper(i, tree, '') for i in s}
    return ''.join([char_map[i] for i in s]), tree

def decode(code, tree):
    s = []
    tree_ptr = tree
    for i in code:
        tree_ptr = tree_ptr._left if i == '0' else tree_ptr._right
        if tree_ptr.is_leaf():
            s.append(tree_ptr._char)
            tree_ptr = tree
    return ''.join(s)
        

def main():
    s = "the quick brown fox jumps over the lazy dog"
    compressed, tree = encode(s)
    print(compressed)
    print("Compression ratio: {0}".format(len(s) * 8 / len(compressed)))
    print(decode(compressed, tree))


if __name__ == "__main__":
    main()
