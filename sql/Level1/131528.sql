-- 나이 정보가 없는 회원 수 구하기
SELECT count(*)
from user_info
where age is null;