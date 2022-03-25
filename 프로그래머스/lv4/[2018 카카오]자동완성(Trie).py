from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isWord = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord

    def startsWith(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


def solution(words):
    answer = 0
    root = Trie()
    for word in words:
        root.insert(word)

    for word in words:
        cur = root
        cnt = 0
        for i, c in enumerate(word):
            cur = cur.children[c]
            cnt += 1
            if len(cur.children) > 1:
                # print("1",word,c,cnt)
                answer += cnt
                cnt = 0
            elif cur.isWord and not i == len(word) - 1:
                # print("2",word,c,cnt)
                answer += cnt
                cnt = 0

            if i == len(word) - 1:
                if not cur.children:
                    # print("3",word,c,cnt)
                    answer += 1
                else:
                    answer += cnt

    return answer
