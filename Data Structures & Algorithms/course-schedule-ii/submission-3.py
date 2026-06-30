class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort algorithm (no cycles, in order) --> isn't unique
        # Ex) preMap = {0:[1,2], 1:[3], 2:[], 3:[3], 4:[0], 5:[0]}
        # once we hit 2, we don't need anymore prereq's, we add to output, remove 2 from preMap
        preMap = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        # A course has 3 possible states:
            # 1. visited -> course has been added to output, never have to consider it again(crossed out)
            # 2. visiting -> course not added to output, but added to cycle (green path, detects cycle
            # 3. unvisited -> course not added to output or cycle
        
        output = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle: # cycle detected
                return False # terminate algorithm and return empty list
            if course in visited:
                return True # don't need to visit course twice
            
            cycle.add(course)
            for neighbor in preMap[course]:
                if dfs(neighbor) == False: # means we detected a cycle
                    return []
            
            # reset
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        
        
        for course in range(numCourses):
            if dfs(course) == False:
                return [] 
        return output


    
    # runtime: O(V + E) , nodes and edges
    # space: O(V + E), where V is course and E is prereqs