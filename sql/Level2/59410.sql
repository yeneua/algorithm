-- NULL 처리하기
select animal_type, case when (name is null) then "No name" else name end, sex_upon_intake
from animal_ins
order by animal_id;

select animal_type, coalesce(name, "No name"), sex_upon_intake
from animal_ins
order by animal_id;