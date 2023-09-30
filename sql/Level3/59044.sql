-- 오랜 기간 보호한 동물(1)
select i.name, i.datetime
from animal_ins i left outer join animal_outs o on i.animal_id = o.animal_id
where o.datetime is null
order by i.datetime asc
limit 3;