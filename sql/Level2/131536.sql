-- 재구매가 일어난 상품과 회원 리스트 구하기
-- 1. 윈도우 함수 이용
with result as(
    select user_id, product_id, row_number() over(partition by user_id, product_id) number 
    from online_sale
    )
select user_id, product_id
from result
where number = 2
order by user_id asc, product_id desc;

select user_id, product_id
from online_sale
group by user_id, product_id
having count(*) >= 2
order by user_id, product_id desc;