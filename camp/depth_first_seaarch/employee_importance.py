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
        def dfs(employee,findEmployeebyId):
            importance = employee.importance
            for person in employee.subordinates:
                subordinate = findEmployeebyId[person]
                importance += dfs(subordinate,findEmployeebyId)
            
            return importance
        
        findEmployeebyId = {}
        for employee in employees: findEmployeebyId[employee.id] = employee
        
#         def findEmployee(id):
#             for employee in employees:
#                 if employee.id == id: return employee
                
        return dfs(findEmployeebyId[id],findEmployeebyId)