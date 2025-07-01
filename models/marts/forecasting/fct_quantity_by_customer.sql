with base as (
    select
        date_trunc('month', invoice_date) as month,
        customer_id,
        country,
        sum(quantity) as total_quantity
    from {{ ref('stg_online_retail') }}
    where customer_id is not null
    group by 1, 2, 3
)

select * from base
order by month, country, customer_id

