# Solution Walk Through
Question: https://leetcode.com/problems/course-schedule-ii/

## Intuition
I can use two hashmaps: one will store how many direct prerequisites a course needs, and one will store the direct postrequisite courses each prerequisite course has. To find courses that need no presequisit, I'd just need to find any course that is now in in direct prerequisites hashmap, as it will have 0 direct prerequisites. Those courses with no direct prerequisites will be the inital queue for the BFS. If completing any of those courses results in another class to have 0 remaining prerequisites, then add that course to the queue. Continue until either every class is accounted for or the queue becomes empty.

## Approach
- Create a `course_dict` where the key is a course number, and the value is the amount of direct prerequisites are needed to take that course.
- Create a `prerequisites_dict` where the key is a prerequisite course, and the value is a list of all the postrequisite courses.
- Create a queue and store all the courses that have no prerequisites (courses that are not in course_dict). Also store all these courses in the result list.
- If all the courses require no reprequisites, return the result list.
- Otherwise, start a BFS loop. Pop the first element from the queue, and check if it has any postrequisite. If it does, decrement all the postrequisites by 1 for their remaining prerequisites. If there are none left, add that course to the queue as a prerequisite, and continue.
- If the tracker of completed courses reaches `numCourses`, then the result list is completed and can be returned. If the queue empties before this, there is no possible sequence.

## Time Complexity
$O(n + m)$

$n$ is the value of `numCourses`. \
$m$ is the length of `prerequisites`.

## Space Complexity
$O(n + m)$