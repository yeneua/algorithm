-- 카테고리 별 도서 판매량 집계하기

SELECT b.category, sum(s.sales) TOTAL_SALES
from book b
left outer join book_sales s
on b.book_id=s.book_id
where year(s.sales_date) = 2022 and month(s.sales_date) = 1
group by category
order by category;