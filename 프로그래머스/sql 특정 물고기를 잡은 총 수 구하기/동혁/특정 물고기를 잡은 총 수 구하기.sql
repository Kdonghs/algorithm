-- 코드를 작성해주세요
select count(*) as FISH_COUNT
from FISH_INFO as i, FISH_NAME_INFO as n
where i.fish_type = n.fish_type
and n.fish_name in ('BASS','SNAPPER')