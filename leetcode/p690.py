# https://leetcode.com/problems/employee-importance/
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        table = {}
        for e in employees:
            table[e.id] = e
            
        result = table[id].importance
        q = []
        q.append(table[id].subordinates)
        while len(q) > 0:
            ids = q.pop()
            for id_ in ids:
                result += table[id_].importance
                q.append(table[id_].subordinates)
        return result
