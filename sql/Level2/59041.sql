-- 동명 동물 수 찾기
select name, count(*)
from animal_ins
where name is not null
group by name
having count(*) >= 2
order by name;