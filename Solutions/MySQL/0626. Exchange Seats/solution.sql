select 
    case 
        when id = (select max(id) from seat) and id % 2 = 1
            then id
        when id % 2 = 1
            then id + 1
        else
            id - 1
    END as id,
    student
from seat
order by id