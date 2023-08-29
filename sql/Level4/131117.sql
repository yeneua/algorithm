-- 5월 식품들의 총매출 조회하기
select p.product_id, p.product_name, sum(p.price * o.amount) total_sales
from food_product p join food_order o on p.product_id = o.product_id
where year(o.produce_date) = 2022 and month(o.produce_date) = 5
group by p.product_id
order by total_sales desc, p.product_id asc;