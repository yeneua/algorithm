-- 상품 별 오프라인 매출 구하기
select p.product_code, sum(p.price * o.sales_amount) sales
from product p join offline_sale o on p.product_id = o.product_id
group by p.product_code
order by sales desc, p.product_code;

select  a.product_code PRODUCT_CODE, a.price * sum(b.sales_amount) SALES 
from product a join offline_sale b on a.product_id = b.product_id
group by product_code
order by SALES desc, PRODUCT_CODE;