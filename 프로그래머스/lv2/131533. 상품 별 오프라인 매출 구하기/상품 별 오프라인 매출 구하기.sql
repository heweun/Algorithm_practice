-- 코드를 입력하세요
SELECT B.PRODUCT_CODE,sum(A.sales_amount*B.price) as SALES
from OFFLINE_SALE A
join PRODUCT B on A.product_id = B.product_id
group by A.product_id
order by SALES desc, PRODUCT_CODE