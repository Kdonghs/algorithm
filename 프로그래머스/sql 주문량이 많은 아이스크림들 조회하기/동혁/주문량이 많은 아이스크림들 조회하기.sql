select F.flavor
from FIRST_HALF AS F, JULY AS J
where F.FLAVOR = J.FLAVOR
group by F.flavor
order by (sum(J.TOTAL_ORDER) + sum(F.TOTAL_ORDER)) desc
limit 3