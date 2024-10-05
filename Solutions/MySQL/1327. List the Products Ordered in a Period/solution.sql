select p.product_name, sum(o.unit) as unit
from products p
inner join orders o on p.product_id = o.product_id
where order_date >= '2020-02-01' and order_date < '2020-03-01'
group by p.product_name
having sum(o.unit) >= 100