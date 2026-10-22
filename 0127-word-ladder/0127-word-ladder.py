from collections import deque
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        def search():
            visited = set()
            wl = set(wordList)
            queue = deque([(beginWord, 0)])
            while queue:
                st ,r = queue.popleft()
                if st == endWord:
                    return r+1
                for i in range(len(st)):
                    for t  in string.ascii_lowercase:
                        new = st[:i] + t+ st[i+1:]
                        if new in wl and new not in visited:
                            visited.add(new)
                            queue.append((new, r+1))

            return 0
        g = search()
        return g