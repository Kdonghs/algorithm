select ID,
       case
           when SIZE_OF_COLONY < 100 then 'LOW'
           when SIZE_OF_COLONY between 100 and 1000 then 'MEDIUM'
           when SIZE_OF_COLONY > 1000 then 'HIGH'
       end as SIZE
FROM ECOLI_DATA 
order by ID;