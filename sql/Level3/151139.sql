-- 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기
select month(start_date) MONTH, car_id, count(*) RECORDS
from car_rental_company_rental_history
where car_id in (select car_id
                from car_rental_company_rental_history
                where month(start_date) between 8 and 10
                group by car_id
                having count(*) >= 5
) and month(start_date) between 8 and 10 -- 메인쿼리 조건 지정
group by month(start_date), car_id
having count(*) != 0
order by 1, 2 desc;

 -- 8~10월 총 대여 횟수가 5번 이상인 car_id를 서브쿼리에서 추출. 메인 쿼리에서 8~10월로 한번더 조건지정.
--  예제를 보면 car_id가 1인 경우, 8~10월 총 대여 횟수 5번이지만 7월에도 대여한 기록이 있음
--  메인 쿼리에서 where절 조건을 지정하지 않았다면 위 경우가 출력됨
