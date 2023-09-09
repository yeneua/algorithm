-- 자동차 대여 기록에서 장기/단기 대여 구분하기
select history_id, car_id, date_format(start_date, "%Y-%m-%d"), date_format(end_date, "%Y-%m-%d"), case when (datediff(end_date,start_date) + 1 >= 30) then "장기 대여" else "단기 대여" end rent_type
from car_rental_company_rental_history
where (year(start_date) = 2022) and (month(start_date) = 9)
order by history_id desc;

-- datediff : 날짜 차이 계산 함수