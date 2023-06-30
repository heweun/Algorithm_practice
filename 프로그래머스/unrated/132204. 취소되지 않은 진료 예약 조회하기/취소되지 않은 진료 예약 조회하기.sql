-- 코드를 입력하세요
#PATIENT 환자번호, 환자이름, 성별코드, 나이, 전화번호
#DOCTOR 의사이름, 의사ID, 면허번호, 고용일, 진료과코드, 전화번호
#APPOINTMENT 진료예약일시, 진료예약번호, 환자번호, 진료과코드, 의사ID, 예약취소여부, 예약취소 날짜
SELECT APNT_NO, B.PT_NAME, A.PT_NO, A.MCDP_CD, C.DR_NAME, APNT_YMD
from APPOINTMENT A
join PATIENT B on A.PT_NO = B.PT_NO
join DOCTOR C on A.MDDR_ID = C.DR_ID

where date_format(APNT_YMD,'%Y-%m-%d') = '2022-04-13'
and APNT_CNCL_YN != "Y"
and A.MCDP_CD = 'CS'

order by APNT_YMD