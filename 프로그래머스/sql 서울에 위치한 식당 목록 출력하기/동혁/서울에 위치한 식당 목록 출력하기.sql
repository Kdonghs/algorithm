-- 코드를 입력하세요
SELECT i.REST_ID, i.REST_NAME, i.FOOD_TYPE, i.FAVORITES, i.ADDRESS, round(avg(r.REVIEW_SCORE),2) as SCORE
from REST_INFO as i, REST_REVIEW as r
where i.REST_ID = r.REST_ID
group by i.REST_ID
having i.ADDRESS like '서울%'
order by SCORE desc, FAVORITES desc