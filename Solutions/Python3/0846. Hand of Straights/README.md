# Solution Walk Through
Question: https://leetcode.com/problems/hand-of-straights/

## Intuition
I first thought to just use a Counter and sort the keys and iterate in order, checking if proper hands can be made. I ran into some edge cases and realized I need a more dynamic sort, so I can use a minheap. The minheap stores the keys, and when the minimum value runs out, it can be popped. If a value other than the minimum value runs out, that creates a gap in the cards and I know the result is false.

## Approach
- Base cases to ensure that the `groupSize` and `hand` length can provide a valid solution
- Create a counter storing the amount of occurences of each card, and create a heap of the keys
- Peek at the minimum value of the heap, and check if it can make a stright of length `groupSize`
- If it can't, return false as there is no way every card can make a stright of length `groupSize`
- If it can, subtract 1 from each cards occurences as it was used
- At the same time, check if each card has no more occurences left
- If there are no more occurences left of a card, and that card is the minimum value, then it can be popped as it has been used
- If there are no more occurences left of a card, and that card is NOT the minimum value, then a gap is created as lower value cards will need that card for a stright, but there are none left, so false can be returned

## Time Complexity
$O(n \log n)$

$n$ is the length of `hands`.

## Space Complexity
$O(n)$