-- ifnull("열","대체할 문자")
-- 오름차순 정렬
SELECT PT_NAME, PT_NO,GEND_CD,AGE,ifnull(TLNO,'NONE') as TLNO
from PATIENT
where AGE<=12 and GEND_CD='W'
order by AGE desc, PT_NAME