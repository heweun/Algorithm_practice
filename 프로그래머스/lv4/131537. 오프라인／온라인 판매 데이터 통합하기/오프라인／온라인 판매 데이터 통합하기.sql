-- 코드를 입력하세요
SELECT date_format(A.SALES_DATE, '%Y-%m-%d') as SALES_DATE, 
A.PRODUCT_ID, A.USER_ID, A.SALES_AMOUNT
from ONLINE_SALE A
where sales_date like '2022-03%'

UNION

SELECT date_format(B.SALES_DATE, '%Y-%m-%d') as SALES_DATE, 
B.PRODUCT_ID, NULL AS USER_ID, B.SALES_AMOUNT
from OFFLINE_SALE B
where sales_date like '2022-03%'

ORDER BY SALES_DATE, PRODUCT_ID, USER_ID