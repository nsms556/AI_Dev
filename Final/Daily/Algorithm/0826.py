# 0826 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060

class TrieNode :
    def __init__(self, data=None) -> None:
        self.data = data
        self.cnt = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.head = TrieNode(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(char)
            current_node.cnt += 1
            current_node = current_node.children[char]

        current_node.cnt += 1

    def search(self, prefix):
        ret = 0
        current_node = self.head

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return 0

        next_node = []
        for c in current_node.children :
            next_node.append(current_node.children[c])

        for i in next_node :
            ret += i.cnt

        return ret

def solution(words, queries) :
    answer = []
    
    trie = [Trie() for _ in range(10000)]
    reverse_trie = [Trie() for _ in range(10000)]

    for word in words :
        trie[len(word)-1].insert(word)
        reverse_trie[len(word)-1].insert(word[::-1])

    for q in queries :
        flag = False
        if q[0] == '?' and q[-1] != '?' :
            flag = True
            q = q[::-1]

        pre = 0
        for i, c in enumerate(q) :
            if c == '?':
                pre = i
                break

        if flag :
            answer.append(reverse_trie[len(q)-1].search(q[:pre]))
        else:
            answer.append(trie[len(q)-1].search(q[:pre]))

    return answer


if __name__ == '__main__' :
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    
    print(solution(words, queries))