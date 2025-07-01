-- models/staging/stg_online_retail.sql

with source as (

    select * from raw_online_retail

),

renamed as (

    select
        cast("Invoice" as varchar) as invoice_id,
        cast("StockCode" as varchar) as product_id,
        cast("Description" as varchar) as description,
        cast("Quantity" as integer) as quantity,
        cast("InvoiceDate" as timestamp) as invoice_date,
        cast("Price" as double) as price,
        cast("Customer ID" as varchar) as customer_id,
        cast("Country" as varchar) as country,
        quantity * price as revenue

    from source
    where quantity > 0
      and price > 0
      and "Customer ID" is not null

)

select * from renamed
