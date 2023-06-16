-- 코드를 입력하세요
SELECT A.animal_id, A.name
from ANIMAL_OUTS A
left join ANIMAL_INS B on A.animal_id = B.animal_id
where B.animal_id is null