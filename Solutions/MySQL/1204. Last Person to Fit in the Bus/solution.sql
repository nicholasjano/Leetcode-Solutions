with CTE as (
    select person_name, sum(weight) over (order by turn) as cumulative_weight
    from queue
)

select person_name
from CTE
where cumulative_weight <= 1000
order by cumulative_weight desc
limit 1