-- 코드를 입력하세요
select USER_ID, PRODUCT_ID
from ONLINE_SALE
group by user_id, product_id
having count(*)>=2
order by user_id, product_id desc