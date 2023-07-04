-- 코드를 입력하세요
#CAR_RENTAL_COMPANY_CAR 대여 중인 자동차들의 정보
 #자동차 ID, 자동차 종류, 일일 대여 요금, 자동차 옵션 
#CAR_RENTAL_COMPANY_RENTAL_HISTORY 자동차 대여 기록 정보
 #자동차 대여 기록ID, 자동차ID, 대여 시작일, 대여 종료일
#CAR_RENTAL_COMPANY_DISCOUNT_PLAN 자동차 종류 별 대여 기간 종류 별 할인 정책
 #요금할인 정책ID, 자동차 종류, 대여 기간 종류, 할인율(7일 이상|30일 이상|90일 이상 만)
 
WITH value AS (
    SELECT car.daily_fee, car.car_type, his.history_id,
           DATEDIFF(end_date, start_date) + 1 AS period,
    CASE 
      WHEN DATEDIFF(end_date, start_date) + 1 >= 90 THEN '90일 이상'
      WHEN DATEDIFF(end_date, start_date) + 1 >= 30 THEN '30일 이상'
      WHEN DATEDIFF(end_date, start_date) + 1 >= 7 THEN '7일 이상'
      ELSE 'NONE' END AS duration_type
FROM car_rental_company_rental_history AS his
INNER JOIN car_rental_company_car AS car ON car.car_id = his.car_id
WHERE car.car_type = '트럭')   



SELECT value.history_id, 
    ROUND(value.daily_fee * value.period * 
          (100 - IFNULL(plan.discount_rate,0)) / 100) AS FEE
FROM value
LEFT JOIN car_rental_company_discount_plan AS plan 
    ON plan.duration_type = value.duration_type 
    AND plan.car_type = value.car_type
ORDER BY 2 DESC, 1 DESC
