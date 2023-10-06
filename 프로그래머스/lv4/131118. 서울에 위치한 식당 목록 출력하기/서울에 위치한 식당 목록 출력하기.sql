-- 코드를 입력하세요
SELECT B.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS,
round(avg(B.REVIEW_SCORE),2) as SCORE
from REST_INFO A
join REST_REVIEW B on A.REST_ID = B.REST_ID
where A.ADDRESS like '서울%'
group by B.rest_id
order by SCORE desc, A.FAVORITES desc