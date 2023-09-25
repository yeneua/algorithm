-- 3월에 태어난 여성 회원 목록 출력하기
select member_id, member_name, gender, date_format(date_of_birth, '%Y-%m-%d')
from member_profile
where tlno is not null and month(date_of_birth) = 3 and gender = 'W'
order by member_id;