-- 12세 이하인 여자 환자 목록 출력하기
select pt_name, pt_no, gend_cd, age, coalesce(tlno, 'NONE') tlno
from patient
where age <= 12 and gend_cd = "W"
order by age desc, pt_name;