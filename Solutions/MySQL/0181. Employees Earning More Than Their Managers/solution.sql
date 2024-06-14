select e.name as Employee
from employee m
inner join employee e on m.id = e.managerid
where e.salary > m.salary