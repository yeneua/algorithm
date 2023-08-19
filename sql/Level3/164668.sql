-- 조건에 맞는 사용자와 총 거래금액 조회하기
select b.writer_id, u.nickname, sum(b.price) total_sales
from used_goods_board b join used_goods_user u on b.writer_id = u.user_id
where b.status = "DONE"
group by b.writer_id
having total_sales >= 700000
order by total_sales asc;