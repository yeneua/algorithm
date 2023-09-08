-- 특정 옵션이 포함된 자동차 리스트 구하기
select *
from car_rental_company_car
where options like "%네비게이션%"
order by car_id desc;