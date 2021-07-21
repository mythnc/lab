# https://leetcode.com/problems/push-dominoes/submissions/
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ary = list(dominoes)
        current_index = 0
        while current_index < len(ary):
            if ary[current_index] == "L":
                for i in range(current_index-1, -1, -1):
                    if ary[i] != ".":
                        break
                    ary[i] = "L"
                
            if ary[current_index] == "R":
                start_index = current_index
                current_index += 1
                while current_index < len(ary) and ary[current_index] == ".":
                    current_index += 1
                if current_index == len(ary):
                    for i in range(start_index, current_index):
                        ary[i] = "R"
                elif ary[current_index] == "R":
                    for i in range(start_index, current_index):
                        ary[i] = "R"
                    continue
                elif ary[current_index] == "L":
                    end_index = current_index
                    while start_index < end_index:
                        ary[start_index] = "R"
                        ary[end_index] = "L"
                        start_index += 1
                        end_index -= 1
                        
            current_index += 1
        return "".join(ary)
