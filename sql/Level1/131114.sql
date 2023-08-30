-- 경기도에 위치한 식품창고 목록 출력하기
select warehouse_id, warehouse_name, address,
    case when freezer_yn = 'Y' then 'Y'
    when freezer_yn='N' then 'N'
    else 'N' end as freezer_yn
from food_warehouse
where address like '경기도%'
order by warehouse_id asc;

-- 다른 풀이
select warehouse_id, warehouse_name, address, coalesce(freezer_yn, 'N') -- coalesce : 지정한 표한식들 중에 NULL이 아닌 첫번째 값 반환
from food_warehouse
where address like '경기도%'
order by warehouse_id asc;