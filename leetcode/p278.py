# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        start_i = 1
        end_i = n
        while True:
            index = (start_i + end_i) // 2
            isBad = isBadVersion(index)
            if isBad and not isBadVersion(index-1):
                return index
            elif not isBad:
                start_i = index + 1
            elif isBad and isBadVersion(index-1):
                end_i = index - 1
