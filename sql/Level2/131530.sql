-- 가격대 별 상품 개수 구하기
select concat(substring(price,1,1), "0000") price_group, count(*) products
from product
group by concat(substring(price,1,1), "0000")
order by price asc;

-- 다른 풀이
select truncate(price, -4) price_group, count(*) products -- truncate(숫자, 버릴 자릿수)
from product
group by price_group
order by price_group;
