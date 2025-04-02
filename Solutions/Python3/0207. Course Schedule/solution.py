class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = {}
        prerequisites_dict = {}
        for a, b in prerequisites:
            if a in course_dict:
                course_dict[a] += 1
            else:
                course_dict[a] = 1
            
            if b in prerequisites_dict:
                prerequisites_dict[b].append(a)
            else:
                prerequisites_dict[b] = [a]

        curr_completed = deque([])
        total_completed = 0
        for i in range(numCourses):
            if i not in course_dict:
                curr_completed.append(i)
                total_completed += 1
        
        if total_completed == numCourses:
            return True

        while curr_completed:
            course = curr_completed.popleft()
            if course in prerequisites_dict:
                for postrequisite in prerequisites_dict[course]:
                    course_dict[postrequisite] -= 1
                    if course_dict[postrequisite] == 0:
                        curr_completed.append(postrequisite)
                        total_completed += 1
                        if total_completed == numCourses:
                            return True
            
        return False