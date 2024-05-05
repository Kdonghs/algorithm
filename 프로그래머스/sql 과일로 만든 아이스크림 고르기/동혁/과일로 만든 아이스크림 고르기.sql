SELECT fh.FLAVOR
from FIRST_HALF as fh, ICECREAM_INFO as ii
where fh.FLAVOR = ii.FLAVOR
    and TOTAL_ORDER>3000
    and ii.INGREDIENT_TYPE = 'fruit_based'
order by fh.TOTAL_ORDER desc