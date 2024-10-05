# Solution Walk Through
Question: https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/

## Intuition
The question gives me the idea that I'd need to group by actor_id and director_id. With that, I can get all the rows for the pair. Afterward, I could easily just check if each actor/director group has three or more timestamps together.

## Approach
- Select actor_id, director_id from ActorDirector
- Group by (actor_id, director_id) pair
- Use a having clause to check only pairs that have 3 or more timestamps, meaning they cooperated at least 3 times.