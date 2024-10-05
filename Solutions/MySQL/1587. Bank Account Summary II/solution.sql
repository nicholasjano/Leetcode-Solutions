select u.name, sum(t.amount) as balance
from users u
inner join transactions t on u.account = t.account
group by u.account
having sum(t.amount) > 10000