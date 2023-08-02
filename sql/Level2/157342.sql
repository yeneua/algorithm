-- 자동차 평균 대여 기간 구하기

select car_id, round(avg(datediff(end_date,start_date)+1),1) AVERAGE_DURATION -- 날짜 +1
from car_rental_company_rental_history
group by car_id
having average_duration >= 7
order by average_duration desc, car_id desc;