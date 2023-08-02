-- 조건에 맞는 도서와 저자 리스트 출력하기

select b.book_id BOOK_ID, a.author_name AUTHOR_NAME, date_format(b.published_date, '%Y-%m-%d') PUBLISHED_DATE
from book b left outer join author a on b.author_id=a.author_id
where b.category='경제'
order by published_date asc;