with 
user_raw as (
    select user_id, 
        count(user_id) over(partition by year(joined)) as user_cnt
    from USER_INFO
    where year(joined) = 2021
)

select year(b.SALES_DATE) as year, 
    month(b.SALES_DATE) as month,
    count(distinct b.user_id) as purchased_users,
    round(count(distinct b.user_id)/user_cnt, 1) as purchased_ratio
from user_raw a left join ONLINE_SALE b on a.user_id = b.user_id
where SALES_DATE is not null
group by 1, 2
order by 1, 2



