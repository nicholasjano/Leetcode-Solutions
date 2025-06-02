# Solution Walk Through
Question: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

## Intuition
I can use a sliding window approach. I can use a hashmap to keep track of the occurences of each letter (since there are only 3 letters, this would be considered $O(1)$ space) and if all three of them have an occurence, I can include that substring, as well as any to the right as the question states at least one occurence of each character, and then I can move the left towards the right.

## Approach
- Initialize a hashmap `occurences` to keep track of the occurences of each letter within the current window.
- Start the sliding window with the left pointer being at index 0 and the right pointer iterating through all indicies of `s`.
- At each iteration, increment the character at the right pointer to the `occurences` hashmap by 1.
- Once all characters are in the current window, a valid substring has been found, so the substrings counter is incremented by `(n - right)` to account for the current substring and all to the right.
- Afterward, the left pointer is moved forward, and the new sliding window is evaluated again to see if all characters are in the current window.
- Once the loop has been completed, return the substrings counter.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(1)$