class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visited = set()

        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        # preMap = {0: [1,2], 1:[3,4], 2:[], 3:[4], 4:[]}

        def dfs(course):
            if course in visited: # visited = { 0, 1, 3}
                return False
            
            if preMap[course] == []: # means we're good to move on and track back in our recursive stack
                return True

            visited.add(course) # think about this 
            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False
            
            # reset
            visited.remove(course)
            preMap[course] = []
            return True


        for course in range(numCourses): # 0, 1, 2, 3, 4, 5
            if dfs(course) == False:
                return False
        return True
    
    # dfs stack
    # dfs(0)
        # dfs(1)
            # dfs(3)
                # dfs(4) --> RET True


