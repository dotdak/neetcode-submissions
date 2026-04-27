
with raw as (
    select fail_date as start_date, 'failed' as period_state from failed
    union all 
    select success_date as start_date, 'succeeded' as period_state from succeeded
    order by start_date
), grouped as (
    select period_state, start_date,
        ROW_NUMBER() OVER (ORDER BY start_date) as global_counter,
        ROW_NUMBER() OVER (PARTITION BY period_state ORDER BY start_date) as group_counter
    from raw
    where start_date >= '2019-01-01' and start_date <= '2019-12-31'
)
select period_state, min(start_date) as start_date, max(start_date) as end_date from grouped
group by period_state, global_counter - group_counter
order by start_date;

-- select * from grouped limit 5;