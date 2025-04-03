# Solution Walk Through
Question: https://leetcode.com/problems/word-search/

## Intuition
I can use DFS backtracking to search the grid for a proper sequence. To ensure cells wont be visited twice on one branch, they will be marked with `"#"`. For search pruning, I can first check if it is possible to make the word with the board in terms of character occurences, and I can also make sure to start from whichever end (front or back of word) that has the least occurences, as it will lead to less branches overall.

## Approach
- Create a count of the characters in `word`, and another could of characters in `board`.
- If there is any character in `word` that cannot be fuifilled by the characters in `board`, return False.
- Reverse `word` if the occurences of the final character are less than the first character.
- Loop through each cell in `board` through the DFS.
- Within the DFS, the first base case checks if the row/column indicies are valid, and if the result is the proper next character.
- If the position is the final index of word, return True as the path has been found.
- Otherwise, mark the cell on the board as visited by setting the value to `"#"`, and continue the DFS in all directions.
- If there is no valid path by the end, return False

## Time Complexity
$O(m \cdot n \cdot 3^{w})$

$w$ is the length of `word`.

## Space Complexity
$O(w)$