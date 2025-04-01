# Solution Walk Through
Question: https://leetcode.com/problems/reorganize-string/

## Intuition
I can first get the occurences of each letter in a hashmap. Afterward, I had the idea of storing the occurence-letter pairs in a maxheap, but that would add extra complexity (in this case it is negligible due to there only being 26 characters). Instead, I can create a resulting list of the total string size, get the character with the max occurences, then add it to the result list, stepping by 2 instead of 1 to ensure there will be no connected characters. After the max occurences character is done, I can continue the same pattern for the rest of the characters in any order. Whn I loop back, I start at 1 and step by 2 so I don't overwrite any numbers.

## Approach
- Cover the base case where the string is only one character long, and return the string.
- Create a hashmap to store the occurences of each character. While doing this, keep track of which element has the max occurences.
- If the character with the max occurences will cover more spaces than avaliable for it to not be connected, return `""`.
- Create a result list the length of the final string. Starting at 0, stepping by 2, add the max occurences to the result list until depleted. Once done, maintain the index, and continue the pattern for the rest of the characters in any order.
- Once the index surpasses the resulting list length, loop back, starting at 1 instead of 0 this time.
- Once done, return the concatenation of the result list.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(k)$

$k$ is the amount of avaliable characters (26).