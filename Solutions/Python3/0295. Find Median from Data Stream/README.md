# Solution Walk Through
Question: https://leetcode.com/problems/find-median-from-data-stream/

## Intuition
The trick here is to use two heaps, one min heap and one max heap. This will ensure that the median or two numbers used to calculate the median and able to be peeked in $O(1)$ time.

## Approach
- `__init__()`:
    - Initialize a maxheap to store the lower half of the data stream, and a minheap to store the upper half of the data stream.
- `addNum()`:
    - Push the value into the lower half, and then pop a value from the lower half into the higher half. Ensure that the lower half always has a length equal to or greather than the higher half to maintain easy peek of the median.
- `findMedian()`:
    - If the lower half is larger than the higher half, return the highest value in the lower half. If both are equal length, return the average of the two closes (peekable) numbers from the heaps.

## Time Complexity
`__init__()`: $O(1)$ \
`addNum()`: $O(\log n)$ \
`findMedian()`: $O(1)$ \

$n$ is the length of the data stream.

## Space Complexity
$O(n)$