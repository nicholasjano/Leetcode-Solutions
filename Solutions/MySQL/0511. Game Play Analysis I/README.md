# Solution Walk Through
Question: https://leetcode.com/problems/game-play-analysis-i/

## Intuition
Select from the minimum event date, grouped by player_id

## Approach
- Select player_id and the minimum event_date from the Activity table
- Group by player_id to ensure that the minimum event_date (first_login) for each player is returned