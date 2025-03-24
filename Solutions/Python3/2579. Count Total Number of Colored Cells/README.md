# Solution Walk Through
Question: https://leetcode.com/problems/count-total-number-of-colored-cells

## Intuition
I need to find a mathematical pattern that describes how the colored cells spread over time. I can start by analyzing what happens at each minute:

- Minute 1: Color 1 cell -> Total: 1 cell
- Minute 2: Color 4 more cells (neighbors of the first cell) -> Total: 5 cells
- Minute 3: Color 8 more cells (outer perimeter) -> Total: 13 cells
- Minute 4: Color 12 more cells (next perimeter) -> Total: 25 cells

I noticed that each minute after the first, we add 4 more cells than the previous minute (4, then 8, then 12, etc.). This follows the pattern of adding $4 \cdot (n - 1)$ new cells at each minute `n`.

This gives me the arithmetic series formula: $1 + (4 \cdot 1) + (4 \cdot 2) + ... + (4 \cdot (n − 1))$

This can be simplified to: $1 + 4 \cdot (1 + 2 + ... + (n − 1))$

Which can be simplified to: $1 + 4 \cdot \frac{(n - 1) \cdot n}{2}$

Which finally results in: $2 \cdot n \cdot (n - 1) + 1$

## Approach
- Return the mathematical representation of the problem, which is `2 * n * (n - 1) + 1`

## Time Complexity
$O(1)$

## Space Complexity
$O(1)$