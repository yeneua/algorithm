-- 주문량이 많은 아이스크림들 조회하기
with result as (
    select f.flavor, sum(f.total_order) + sum(j.total_order) sum
    from first_half f right outer join july j on f.flavor = j.flavor
    group by f.flavor, j.flavor
    order by sum desc
    limit 3
)
select flavor
from result;