# Solution Walk Through
Question: https://leetcode.com/problems/median-of-two-sorted-arrays/

## Intuition
I first thought to just combine the lists then find the median, but then I realized the solution needs to be in $O(\log (m+n))$, so I needed to find another solution. The presence of log tells me I need to use binary search. What I can do is calculate the halfway point of the overall lists combined length, and use that halfway point as my left partition length. From there, I can run binary search on the smaller list. The left partition length will be used to create the combined left partition for the lists by taking the current binary search position, and doing left partition length - current binary search position for the larger list position. By doing this, I can create a left partition using both lists at different positions, but the combined length is the proper left partition length. From there, I can move across the smaller list until I find the proper position where I have all the smaller-half numbers, and then I can get the median.

## Approach
- Calculate the total length of both lists as `total`, and the midway point (left partition length) as `half`.
- Reassign `nums1` and `nums2` so `large` and `small` based off the size of the lists.
- Complete a binary search on `small`, with proper `mid` calculations. The number in `small` at index `mid` will be the final number of the left partition for `small` for the check.
- To get the total left partition from both lists, do `complement = (half - 1) - (mid + 1)`, where the number in `large` at index `complement` will be the final number of the left partition for `large` for the check. This means that `small` up to `mid`, and `large` up to `complement` combine for the left partition.
- Check if the left partition contains the proper numbers:
    - If both the small number is less than the next large number, and the large number is less than the next small number, this is the proper left partition, meaning the median is either the smallest next number (for odd), or the average of the current largest number and smallest next number (for even). This is the return statement.
    - If the small number is greater than the next large number, that means there needs to be less numbers from the small list in the left partition, so the binary search can continue with `right = mid - 1`
    - If the large number is greater than the next small number, that means there needs to be more numbers from the small list in the left partition, so the binary search can continue with `left = mid + 1`
- For edge cases where the whole left partition comes from one list or one whole list is within the left partition, infinite values are used to ensure proper handling.

## Time Complexity
$O(\log (m+n))$

## Space Complexity
$O(1)$