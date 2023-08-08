-- 헤비 유저가 소유한 장소
with results as (
select *, row_number() over(partition by host_id) as num -- 윈도우 함수 이용
from places)
select id,name, host_id
from places
where host_id in (select host_id from results where num >= 2) -- 서브 쿼리
order by id asc;


-- 다른 풀이
select *
from places
where host_id in ( -- 서브 쿼리 이용
    select host_id
    from places
    group by host_id
    having count(*) > 1)
order by id;