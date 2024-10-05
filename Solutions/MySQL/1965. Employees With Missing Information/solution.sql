select e.employee_id
from employees e
left join salaries s on e.employee_id = s.employee_id
where s.salary is null
union
select s.employee_id
from employees e
right join salaries s on e.employee_id = s.employee_id
where e.name is null
order by employee_id asc;