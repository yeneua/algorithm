-- 가격이 제일 비싼 식품의 정보 출력하기
select *
from food_product
where price = (select max(price) from food_product);

select *
from food_product
order by price desc
limit 1;
