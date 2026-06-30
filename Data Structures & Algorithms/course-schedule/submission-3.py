class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # represent as graph where cycle indicates impossible because of pre-req requirement
        # Data Structure: adjacency list --> preMap = {}

        #  run DFS on every node from 0 to n-1.
        # if a node can be successfully completed, we move it from the preMap

        # Ex) prereq = [[0,1],[0,2],[1,3],[1,4],[3,4]], n = 5
        preMap = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre) # {0:[1, 2], 1:[3, 4], 2:[], 3:[4], 4:[]}
        
        visited = set() # visited = ()

        def dfs(course):
            if course in visited:
                return False

            if preMap[course] == []:
                return True
            
            visited.add(course)
            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False
            
            # reset after we've successfully processed a course
            visited.remove(course)
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True

    # Runtime: O(Nodes + Prereqs)
