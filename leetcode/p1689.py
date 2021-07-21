# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/submissions/
class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(c) for c in n])
