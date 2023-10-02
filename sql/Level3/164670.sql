-- 조건에 맞는 사용자 정보 조회하기
select u.user_id user_id, u.nickname nickname,
       concat(u.city, ' ', u.street_address1,' ', u.street_address2) 전체주소, -- 공백 넣기
       concat(substring(u.tlno, 1,3), '-', substring(u.tlno, 4, length(u.tlno) - 7), '-', substring(u.tlno, -4, 4)) 전화번호 -- 중간 자리가 3자리인 경우도 고려
from used_goods_board b join used_goods_user u on b.writer_id = u.user_id
group by u.user_id
having count(*) >= 3
order by 1 desc;

-- substring(문자열, 시작, 길이) 시작이 음수일 경우 오른쪽부터 리턴

-- concat_ws() : 사용자가 지정한 것을 구분자로 구분한 뒤 결합
-- concat_ws(' ', u.city, u.street_address1, u.street_address2)
-- concat_ws('-', substring(u.tlno, 1,3), substring(u.tlno, 4, length(u.tlno) - 7), substring(u.tlno, -4, 4)) 