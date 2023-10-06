#임시 테이블 만들기
WITH DISCOUNT AS(SELECT A.DAILY_FEE, A.CAR_TYPE, B.HISTORY_ID,
                 DATEDIFF(END_DATE, START_DATE)+1 AS PERIOD,
                 CASE
                 WHEN DATEDIFF(END_DATE, START_DATE)+1>=90 THEN '90일 이상'
                 WHEN DATEDIFF(END_DATE, START_DATE)+1>=30 THEN '30일 이상'
                 WHEN DATEDIFF(END_DATE, START_DATE)+1>=7 THEN '7일 이상'
                 ELSE 'NONE'
                 END AS duration_type
                 
                FROM CAR_RENTAL_COMPANY_CAR A
                JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B ON A.CAR_ID=B.CAR_ID
                WHERE A.CAR_TYPE = '트럭')

#임시 테이블과 새로 JOIN하기
SELECT D.HISTORY_ID,
ROUND(DAILY_FEE * PERIOD * (1 - IFNULL(discount_rate,0) * 0.01), 0) AS FEE
FROM DISCOUNT D
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C ON D.CAR_TYPE = C.CAR_TYPE
AND D.duration_type = C.duration_type
ORDER BY FEE DESC, D.HISTORY_ID DESC