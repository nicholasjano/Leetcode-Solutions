# Solution Walk Through
Question: https://leetcode.com/problems/reconstruct-itinerary/

## Intuition
In a hashmap, for each airport, I can hold the visitable airports as their value. I can create a stack and start it with JFK. I can use DFS afterward to build the route.

## Approach
- Create a hashmap, with the keys being the start destination airports of each ticket, and the values being all the possible destinations from that airport. The tickets are sorted lexicographically.
- Initialize the route list and stack, starting with JFK.
- For the last index of the stack, add all their destinations to the back of the stack in lexical order
- Whichever airport is now at the back of the stack gets popped into routes
- Continue this until all tickets have been accounted for. I then reversed routes for the final itinerary.

## Time Complexity
$O(n \log n)$

## Space Complexity
$O(n)$