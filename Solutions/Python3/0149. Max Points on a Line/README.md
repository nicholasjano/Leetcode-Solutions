# Solution Walk Through
Question: https://leetcode.com/problems/max-points-on-a-line/

## Intuition
I can utilize the slope formula of $\frac{y_{2} - y_{1}}{x_{2} - x_{1}}$ to get the slope between each pair of points. Using normalization, I can figure out which points all have the same slone with eachother, and store the max value.

## Approach
- Cover the base case if `points` has 2 or less points, just return the length. Any 2 unique points can form a line.
- Loop through each point as the starting point. Within that, a nested loop is done for every other point to each each point pair combination. Each point will initialize its own `slopes` dictionary.
- For each pair, calculate `dy` and `dx` for the slope. If the slope is horizontal or vertical, cover the base cases.
- Otherwise, the GCD of `dy` and `dx` needs to be found, and `dy` and `dx` need to be divided by it to normalize `dy` and `dx`. This is primarily to avoid floating point division. To ensure proper direction, ensure `dx` is always positive.
- Once the normalized `dy` and `dx` pair has beed found for the points, increment the `slopes` value at the key of the pair. Keep track of the maximum value.
- Run this loop for each point, always keeping track of the maximum value for a single slope from a single point.
- Once the loop has completed, return the maximum value

## Time Complexity
$O(n^{2})$

$n$ is the length of `points`.

## Space Complexity
$O(n)$