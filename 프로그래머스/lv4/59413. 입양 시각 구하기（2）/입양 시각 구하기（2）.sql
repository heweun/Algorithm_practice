-- 코드를 입력하세요
#시간대가 7~19시 밖에 없음-->없는 시간대를 만들어 줘야함
WITH RECURSIVE blank AS ( #빈 가상의 테이블 만들기
    SELECT 0 AS HOUR #select 0 as hour-> 0이 데이터인 hour변수 생성
    UNION ALL #데이터 0~23으로 늘리기
    SELECT HOUR + 1 #hour(0이 시작)+1
      FROM blank 
     WHERE HOUR < 23 #hour이 22가 될때 까지
)

#select * from blank #가상의 테이블 출력

select hour, count(hour(a.datetime)) as count
from blank b
left join animal_outs a on b.hour = hour(a.datetime)
group by b.hour
order by b.hour