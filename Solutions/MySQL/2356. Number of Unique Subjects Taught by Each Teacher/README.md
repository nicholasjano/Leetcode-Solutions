# Solution Walk Through
Question: https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/

## Intuition
By using distinct, we can easily count the amount of unique subjects each teacher teaches in the university.

## Approach
- Select teacher_id, count(distinct subject_id) from Teacher. The term count(distinct subject_id) will give the count of unique subjects.
- Group by teacher_id to ensure the count of distinct subject_id's are calculated per teacher.