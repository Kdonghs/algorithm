-- 코드를 작성해주세요
-- ifnull 앞 파라미터가 null이면 뒷 파라미터로 대체
select ID,
       IFNULL(
               (
                   SELECT COUNT(*)
                   FROM ECOLI_DATA
                   GROUP BY PARENT_ID
                   HAVING PARENT_ID = ID
               ), 0
           ) AS CHILD_COUNT
from ECOLI_DATA
order by id