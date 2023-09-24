-- 성분으로 구분한 아이스크림 총 주문량
select i.ingredient_type, sum(f.total_order) total_order
from icecream_info i join first_half f on i.flavor = f.flavor
group by i.ingredient_type
order by total_order;