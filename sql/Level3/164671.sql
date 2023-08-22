-- 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기
select concat("/home/grep/src/", b.board_id, "/", f.file_id, f.file_name, f.file_ext) file_path
from used_goods_board b join used_goods_file f on b.board_id = f.board_id
where views = (select max(views) from used_goods_board)
order by f.file_id desc;