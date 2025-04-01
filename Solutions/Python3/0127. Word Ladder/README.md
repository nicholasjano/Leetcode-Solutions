# Solution Walk Through
Question: https://leetcode.com/problems/word-ladder/

## Intuition
I can use a bidirectional BFS approach starting from `beginWord` to `endWord` and meeting inbetween. For each word, every possible variation based on the alphabet will be check to determine if it exists in `wordList`. If it has not been visited yet, add it to the BFS queue and continue. Once both BFS paths have visited the same word, then the transformation sequence has been found.

## Approach
- Cover the base case for when `endWord` is not in `wordList`, as this will always be 0.
- Crete two BFS queues, one from `beginWord` and one from `endWord`. Two visited hashmaps are also made respectively, that keep track of the distance traveled to reach any given word.
- While the queues still have values, run BFS on the current level of the shortest queue.
- Within the BFS, create every possible work variation, and check if any are in `wordSet` but have yet to be visited. If one is found, add it to visited and the queue.
- If a word has been reached by both BFS paths, than a full transformation sequence has been found, the and distances can be returned.

## Time Complexity
$O(n \cdot L)$

$n$ is the length of `wordList`. \
$L$ is the length of `beginWord`.

## Space Complexity
$O(n \cdot L)$
