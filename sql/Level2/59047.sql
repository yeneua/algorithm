-- 이름에 el이 들어가는 동물 찾기
select animal_id, name
from animal_ins
where name like "%el%" and animal_type = "Dog"
order by name;