-- models/audit/audit_valid_online_retail.sql

with raw as (
    select *, "InvoiceDate"::DATE as invoice_date from raw_online_retail
),

valid as (
    select *
    from raw
    where
        "Customer ID" is not null
        and Quantity > 0
        and Price > 0
),

aggregated as (
    select
        invoice_date,
        "Country" as country,
        count(*) as valid_transactions,
        sum(Quantity * Price) as total_revenue
    from valid
    group by 1, 2
)

select * from aggregated
