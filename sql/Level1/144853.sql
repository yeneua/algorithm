-- 조건에 맞는 도서 리스트 출력하기
SELECT book_id, date_format(published_date, '%Y-%m-%d')
from book
where year(published_date)="2021" and category = '인문'
-- published_date like "2021%" 이 구문으로도 동일한 결과 나오지만 date 타입이니 year로 지정해주는 게 더 좋을 듯 !(내 생각)
order by published_date asc;