-- 코드를 입력하세요
SELECT distinct A.car_id
from CAR_RENTAL_COMPANY_CAR A
join CAR_RENTAL_COMPANY_RENTAL_HISTORY B on A.CAR_ID = B.CAR_ID
where car_type = '세단'
and month(start_date) = 10 
order by A.car_id desc