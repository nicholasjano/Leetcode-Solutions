# Solution Walk Through
Question: https://leetcode.com/problems/triangle-judgement/

## Intuition
To have a triangle with three line segments, they'd need to follow the formula: x+y>z and y+z>x and z+x>y

## Approach
- Select * (x, y, z columns) from Triangle
- In addition, I also select based off an if statemenet that determines whether the lengths can make a triangle. This condition is: x+y>z and y+z>x and z+x>y.