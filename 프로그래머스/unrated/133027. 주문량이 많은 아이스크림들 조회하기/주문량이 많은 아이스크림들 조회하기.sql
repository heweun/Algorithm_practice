-- 코드를 입력하세요
select H.FLAVOR #, sum(H.total_order+J.total_order) as total
from FIRST_HALF H
join (select Flavor, sum(total_order) as total_order
     from july
     group by flavor) J
on H.flavor = J.flavor
group by flavor
order by sum(H.total_order+J.total_order) desc
limit 3