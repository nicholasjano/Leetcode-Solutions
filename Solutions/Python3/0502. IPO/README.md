# Solution Walk Through
Question: https://leetcode.com/problems/ipo

## Intuition
Capital will be an important foactor in this question, as many projects will be not be avaliable for certain w values. We can sort for this, and pait it with it's cooresponding
profit value. Afterward, we can create a maxheap to store the profits of all avaliable projects, adding to it when our w increases.

## Approach
- Check the base case of k = 0, and just return w if true
- Create a projects list with a tuple for the profit capital pair of each project
- Sort projects by capital in descending order, so the lowest capital will be at the end of the list.
- Create a heap. This will be used to store profits of all avaliable projects
- For each k, we find the most profitable avaliable project, and add the profits to w.
- To do this, we push all the profits of the avaliable projects to the heap (negative values to emulate a maxheap on python). Afterward, we pop the highest profit project from the heap, and add it to w.

## Time Complexity
$O(n \log n + k \log n)$

## Space Complexity
$O(n)$