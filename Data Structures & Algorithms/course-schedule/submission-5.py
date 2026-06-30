class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        # preMap = {0:[], 1:[], 2:[], 3:[], 4:[]}
        visited = set() #in this solution, visited means “currently in the DFS path (recursion stack)”, not “seen at any time”.

        def dfs(course):
            if course in visited:
                return False

            if preMap[course] == []: # means we're good to move on and track back in our recursive stack
                return True
            
            visited.add(course) # visited = {}
            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False
            
            # After we've successfully verified all prerequisites for course, we reset:
            visited.remove(course)
            preMap[course] = []
            return True
        
        for course in range(numCourses): # i = 0, 1, 2, 3, 4
            if dfs(course) == False :
                return False
        return True
    
    # dfs stack
    # dfs(0) --> RET True
        # dfs(1) --> RET True
            # dfs(3) --> RET True
                # dfs(4) --> RET True
    # dfs(2) --> RET True


