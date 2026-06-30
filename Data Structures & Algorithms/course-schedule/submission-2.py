class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # represent as graph where cycle indicates impossible because of pre-req requirement
        # Data Structure: adjacency list --> preMap = {}

        #  run DFS on every node from 0 to n-1.
        # if a node can be successfully completed, we move it from the preMap

        # Runtime: O(Nodes + Prereqs)
        preMap = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if preMap[course] == []:
                return True
            
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            
            # reset
            visited.remove(course)
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True

