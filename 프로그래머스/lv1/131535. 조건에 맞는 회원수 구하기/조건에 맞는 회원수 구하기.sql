-- 코드를 입력하세요
SELECT count(USER_ID) as USERS
from USER_INFO
where JOINED like "2021%"
and age>= 20 and age<=29