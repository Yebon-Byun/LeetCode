from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False
    
    def add_word(self, word):
        cur = self
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end_word = True
            


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.add_word(word)

        ROWS, COLS = len(board), len(board[0])
        visit, res = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                (r, c) in visit or
                board[r][c] not in node.children):
                return


            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_end_word:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)