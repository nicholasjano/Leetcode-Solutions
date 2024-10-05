# Solution Walk Through
Question: https://leetcode.com/problems/article-views-i/

## Intuition
Since the ids for an author and viewer are the same, I can just check the condition where author_id = viewer_id.

## Approach
- Select distinct author_id the Views table, distinct is used to ensure there are no duplicates for people who viewed their own article more than once
- Use a where clause of author_id = viewer_id to ensure that the viewer is the author
- Afterward, just order by author_id ascending