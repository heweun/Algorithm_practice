-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME,
case 
when SEX_UPON_INTAKE like '%Spayed%' 
or SEX_UPON_INTAKE like '%Neutered%' then 'O' 
else 'X' end as 중성화

from ANIMAL_INS
ORDER BY ANIMAL_ID;