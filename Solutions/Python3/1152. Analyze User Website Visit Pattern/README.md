# Solution Walk Through
Question: https://leetcode.com/problems/analyze-user-website-visit-pattern/

## Intuition
I can use a brute force solution. First, I can get the websites visited per user, with their respective timestamps. Then, for each user, sort their visits are create every possible triplet, and place them in a set to ensure no duplicates. Afterward, add the triplets to a counter, and keep track of the max triplet.

## Approach
- Create a hashmap to store each user as the key, and the websites they visited as the value. Pair the websites visited with their respective timestamp for ordering.
- For each user, first sort their visits by timestamp.
- Afterward, create a triple-nested for loop to create every possible triplet. Place the triplets in a set to avoid duplicates.
- With the triplets set, increment each triplet on a triplet counter hashmap. Keep track of the max triplet.
- Once completed for every user, return the max triplet.

## Time Complexity
$O(n^{3})$

$n$ is the length of `usernames`.

## Space Complexity
$O(n^{3})$