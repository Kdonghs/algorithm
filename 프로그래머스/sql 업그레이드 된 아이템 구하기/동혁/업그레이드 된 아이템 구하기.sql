-- 코드를 작성해주세요
select i.ITEM_ID, i.ITEM_NAME, i.RARITY
from ITEM_INFO as i, ITEM_TREE as t
where i.ITEM_ID = t.ITEM_ID
and 1=1
and t.PARENT_ITEM_ID in (select ITEM_ID
                        from ITEM_INFO
                        where RARITY='RARE')
order by i.ITEM_ID desc