# Solution Walk Through
Question: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

## Intuition
It is a pretty simple sliding window problem to figure out the count of substrings containing every vowel and AT LEAST `k` consonants. Knowing this, I can use use an approach to find at least `k` consonants, and subtract it by substring with at least `k + 1` consonants, which would give the count of substrings containing every vowel and exactly `k` consonants. To do this, I can use a hashmap to keep track of the vowel counts, and a variable to keep track of the consonants count, and move the left and right pointers to cover all possible valid substrings and their extensions.

## Approach
- Create a helper function `atLeastK()` to compute the count of substrings containing every vowel and AT LEAST k consonants.
- Within this function, first setup a dictionary to hold to vowel counts, and a variable to hold the consonant (non-vowel) count.
- Create a left pointer at index 0 and a right pointer iterating from 0 to `n` for the sliding window.
- For each iteration, grab the character at the right index, determine whether it is a vowel or not and account for it accordingly.
- If at any iteration the window contains all vowels and at least k non-vowels, this is a valid substring and new logic will need to be applied:
    - Increment the total substring count by `(n - right)` as anything to the right of the substring will just add characters and will also be valid.
    - Shift the left pointer by one and correctly remove it from either the vowels dictionary or the non vowel counter, and check again if the current window holds a valid substring.
- By the end, return the total substring count.
- Return `atLeastK(k) - atLeastK(k + 1)` to ensure that only the substrings with exactly `k` consonants count.

## Time Complexity
$O(n)$

$n$ is the length of `word`.

## Space Complexity
$O(1)$