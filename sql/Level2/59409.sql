-- 중성화 여부 파악하기
select animal_id, name, case when (sex_upon_intake like "Neutered%") then "O"
                             when (sex_upon_intake like "Spayed%") then "O" else "X" end 중성화
from animal_ins
order by animal_id;