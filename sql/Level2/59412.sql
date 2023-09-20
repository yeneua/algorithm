-- 입양 시각 구하기(1)
select hour(datetime), count(*)
from animal_outs
where hour(datetime) between 9 and 19
group by hour(datetime)
order by hour(datetime);