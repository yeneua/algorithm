-- 조건에 맞는 회원수 구하기
select count(*)
from user_info
where year(joined) = 2021 and (age between 20 and 29);