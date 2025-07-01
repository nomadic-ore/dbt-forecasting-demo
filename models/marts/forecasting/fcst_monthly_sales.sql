-- models/marts/forecasting/fcst_monthly_sales.sql

with base as (

    select
        date_trunc('month', invoice_date) as month,
        country,
        count(distinct invoice_id) as num_orders,
        count(distinct customer_id) as num_customers,
        sum(quantity * price) as total_revenue,
        sum(quantity) as total_units
    from {{ ref('stg_online_retail') }}
    group by 1, 2

)

select * from base
order by month, country
