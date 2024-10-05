# Solution Walk Through
Question: https://leetcode.com/problems/average-time-of-process-per-machine/

## Intuition
Since I'm looking for the average time of process per machine, I know I'd need to group by machine_id. I can use an if statement to sum all the (end - start) values, and then divide by the amount of processes for the average.

## Approach
- Select machine_id from activity.
- Included in the select is the fomula for calculating average processing_time.
- The first step to calculate the processing_time is to sum all the processing times, where the end is positive and start is negative. This finds the difference from end to start, which is the processing time.
- The next step would be to divide that sum by the amount of processes, and round the final result to 3 decimal places.
- Group by machine_id to ensure every calculation is done individually for each machine.