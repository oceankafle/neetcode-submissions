class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)} # be able to map the courses to their pre-reqs
        visited = set() # keep track of what we've seen so far in the recursive stack

        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        # preMap = {0:[1, 2], 1:[3, 4], 2:[], 3:[4], 4:[]}

        def dfs(course):
            if course in visited:
                return False # means we've detected a cycle 
            
            if preMap[course] == []:
                return True
            
            visited.add(course)
            for neighbor in preMap[course]:
                if dfs(neighbor) == False:
                    return False
            
            # resetting logic after we've processed all pre-reqs
            visited.remove(course)
            preMap[course] = [] # everything after this course has been processed succesfully and works
            return True 


        for course in range(numCourses): # how to call our dfs recursive function
            if dfs(course) == False:
                return False
        return True