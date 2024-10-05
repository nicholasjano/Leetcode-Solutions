# Solution Walk Through
Question: https://leetcode.com/problems/daily-leads-and-partners/

## Intuition
The question is pretty self-explanitory here, just some basic count() aggregations need to be used, while grouping by the pair of (date_id, make_name).

## Approach
- Select date_id and make_name from dailysales
- Included in the select are two aggregations, one for the count of unique lead_id values and one for the count of unique partner_id values.
- Group by the pair of (date_id, make_name) to ensure the aggregations get the correct values.