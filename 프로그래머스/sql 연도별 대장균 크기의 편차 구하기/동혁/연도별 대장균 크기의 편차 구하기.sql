-- 코드를 작성해주세요
--최대 크기를 가진 테이블을 생성해서 비교
select YEAR(A.DIFFERENTIATION_DATE) as YEAR,
    B.YEAR_MAX - A.SIZE_OF_COLONY as YEAR_DEV,ID
from ECOLI_DATA as a,
    (select YEAR(DIFFERENTIATION_DATE) as YEAR, max(SIZE_OF_COLONY) as YEAR_MAX
        from ECOLI_DATA
        group by YEAR) as b
where year(a.DIFFERENTIATION_DATE) = b.YEAR
order by YEAR, YEAR_DEV
