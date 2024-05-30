-- 코드를 작성해주세요
--concat 문자열 붙히기
select concat(LENGTH,'cm') as MAX_LENGTH
from FISH_INFO
order by LENGTH desc
limit 1