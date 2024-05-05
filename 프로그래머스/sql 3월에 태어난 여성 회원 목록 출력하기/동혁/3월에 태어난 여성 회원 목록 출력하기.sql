-- 날짜 출력 포멧
-- 해당 월 조회
SELECT MEMBER_ID,MEMBER_NAME,GENDER,date_format(DATE_OF_BIRTH,"%Y-%m-%d")
from MEMBER_PROFILE
where DATE_OF_BIRTH like "%-03-%"
and GENDER='w'
and TLNO is not null
order by MEMBER_ID