-- 즐겨찾기가 가장 많은 식당 정보 출력하기

with result as (
	select food_type, rest_id, rest_name, favorites,
				 row_number() over(partition by food_type order by favorites desc) as number
	from rest_info) -- 윈도우 함수 이용
select food_type, rest_id, rest_name, favorites
from result
where number = 1
order by food_type desc;

-- 다른 풀이
select food_type, rest_id, rest_name, favorites
from rest_info
where (food_type, favorites) in -- 서브쿼리 사용
(select food_type, max(favorites) from rest_info group by food_type)
order by food_type desc;