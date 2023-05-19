-- 코드를 입력하세요
SELECT year(SALES_DATE) as year, month(sales_date) as month, gender,
count(distinct a.user_id) as users
from USER_INFO A
join ONLINE_SALE B on A.USER_ID = B.USER_ID
where GENDER is  not null
group by year, month, gender
order by year, month, gender