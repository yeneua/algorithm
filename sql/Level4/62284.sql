-- 우유와 요거트가 담긴 장바구니
select a.cart_id
from cart_products a
    inner join cart_products b on a.cart_id = b.cart_id and b.name = "Yogurt" -- mysql은 intersect, minus 연산 지원 X
where a.name = "Milk";