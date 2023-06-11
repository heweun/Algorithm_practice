-- 코드를 입력하세요
select *
from FIRST_HALF H
join july J on H.FLAVOR = J.FLAVOR
where J.FLAVOR = (
    SELECT FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
    from july
    group by FLAVOR
)