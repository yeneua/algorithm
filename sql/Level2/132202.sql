-- 진료과별 총 예약 횟수 출력하기
select mcdp_cd "진료과 코드", count(*) 5월예약건수
from appointment
where year(apnt_ymd) = 2022 and month(apnt_ymd) = 5
group by mcdp_cd
order by 5월예약건수, mcdp_cd;
