-- 코드를 작성해주세요
select c.id, c.GENOTYPE, p.GENOTYPE as PARENT_GENOTYPE
from ECOLI_DATA as p, ECOLI_DATA as c
where c.PARENT_ID = p.id
and (p.GENOTYPE & c.GENOTYPE)=p.GENOTYPE
order by c.id