-- 코드를 작성해주세요
-- &는 비트단위 연산자
-- SKILLCODES의 code가 2진값으로 되어 있음
select d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
from DEVELOPERS as d
where d.SKILL_CODE  & (select CODE from SKILLCODES where name = 'Python')
or d.SKILL_CODE & (select CODE from SKILLCODES where name = 'C#')
order by d.ID