-- 카테고리 별 상품 개수 구하기
select substring(product_code, 1, 2) category, count(*) products
from product
group by category
order by category;