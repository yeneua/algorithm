-- 서울에 위치한 식당 목록 출력하기
select i.rest_id, i.rest_name, i.food_type, i.favorites, i.address, round(avg(r.review_score), 2) score
from rest_info i right outer join rest_review r on i.rest_id = r.rest_id -- 리뷰가 없는 식당은 조회x(리뷰 테이블 기준 right outer join)
where i.address like '서울%' -- 서울로 시작하는 주소
group by i.rest_id
order by score desc, favorites desc;