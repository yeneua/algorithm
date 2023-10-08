-- 취소되지 않은 진료 예약 조회하기
select a.apnt_no, p.pt_name, p.pt_no, d.mcdp_cd, d.dr_name, apnt_ymd 
from patient p join appointment a on p.pt_no = a.pt_no join doctor d on a.mddr_id = d.dr_id
where a.mcdp_cd = 'CS' and a.apnt_cncl_yn = 'N' and date_format(a.apnt_ymd, '%Y-%m-%d') = '2022-04-13'
order by a.apnt_ymd asc;