from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.result = []
        self.end_word = endWord
        self.words = wordList
        self.backtrace(beginWord, [beginWord])

        if len(self.result) == 0:
            return []

        size_ary = [len(ary) for ary in self.result]
        min_len = min(size_ary)
        return [self.result[i] for i, ary in enumerate(size_ary) if ary == min_len]
        
    def backtrace(self, beginWord, path):
        #print(path)
        if self.end_word in path:
            self.result.append(path[:])
            return
        
        for word in self.words:
            if word in path or not self.valid(beginWord, word):
                continue

            path.append(word)
            self.backtrace(word, path)
            path.pop()
        
    def valid(self, s1, s2):
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
            if diff > 1:
                return False
        if diff == 1:
            return True
        return False

print(Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log"]))
print(Solution().findLadders("hot", "dog", ["hot","dog"]))
ary = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
print(Solution().findLadders("qa", "sq", ary))
