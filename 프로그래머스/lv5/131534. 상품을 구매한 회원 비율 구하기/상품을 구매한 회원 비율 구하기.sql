select year(sales_date) as year, #구매 년도
    month(sales_date) as month, #구매 월
    count(distinct A.user_id) as puchased_users, #구매한 사람 수
    # distinct로 중복 없이 개수 세기
    round(count(distinct A.user_id)/(select count(*) from user_info where year(joined)=2021),1) as puchased_ratio
    #1. 2번째 자리에서 반올림 round(A,1)
    #2. 2021년에 가입+그 이후 아무때나 구매 / 2021년 가입
    # select count(*) from user_info where year(joined)=2021 
    # 2021년에 가입된 사람 전체 합계

from online_sale A
join user_info B on A.user_id  = B.user_id 
where year(joined) = 2021
group by year(sales_date),month(sales_date)
order by year,month