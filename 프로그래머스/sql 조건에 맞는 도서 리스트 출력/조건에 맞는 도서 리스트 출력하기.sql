-- 날짜 출력 형식
-- like를 활용한 기간, 카테고리 검색
-- 정렬
SELECT BOOK_ID , DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d')as PUBLISHED_DATE
from BOOK
where published_date like "2021%" and category like '인문'
order by published_date asc