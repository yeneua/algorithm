-- 어린 동물 찾기
-- intake_condition이 Aged가 아닌 경우
select animal_id, name
from animal_ins
where intake_condition != 'Aged'
order by animal_id asc;