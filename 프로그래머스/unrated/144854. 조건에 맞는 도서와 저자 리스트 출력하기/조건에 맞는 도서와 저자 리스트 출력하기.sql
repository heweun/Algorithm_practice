-- 코드를 입력하세요
SELECT BOOK_ID, AUTHOR_NAME, date_format(PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE
from BOOK B
join AUTHOR A on B.AUTHOR_ID = A.AUTHOR_ID
where category = '경제'
order by PUBLISHED_DATE