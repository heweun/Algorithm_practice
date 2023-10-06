-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE,
case
when STATUS = 'SALE' then '판매중'
WHEN status = 'RESERVED' THEN '예약중'
WHEN STATUS = 'DONE' THEN '거래완료'
END AS STATUS

from USED_GOODS_BOARD 
where CREATED_DATE like '2022-10-05%'
ORDER BY BOARD_ID DESC