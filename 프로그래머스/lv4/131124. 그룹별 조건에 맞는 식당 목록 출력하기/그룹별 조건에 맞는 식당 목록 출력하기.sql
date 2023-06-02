-- 코드를 입력하세요
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, 
       Date_format(R.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE M
join REST_REVIEW R on M.MEMBER_ID = R.MEMBER_ID
WHERE M.MEMBER_ID = (
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    ORDER BY COUNT(*) DESC LIMIT 1
)
order by REVIEW_DATE, REVIEW_TEXT

# SELECT A.MEMBER_NAME,B.REVIEW_TEXT,DATE_FORMAT(B.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
# from MEMBER_PROFILE A join REST_REVIEW B
# on A.MEMBER_ID = B.MEMBER_ID
# WHERE A.MEMBER_ID = (SELECT MEMBER_ID FROM REST_REVIEW
# GROUP BY MEMBER_ID
# ORDER BY COUNT(*) DESC LIMIT 1)
# order by REVIEW_DATE asc, REVIEW_TEXT