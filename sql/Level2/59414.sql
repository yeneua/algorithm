-- DATETIME에서 DATE로 형 변환
select animal_id, name, date_format(datetime, "%Y-%m-%d")
from animal_ins
order by animal_id;