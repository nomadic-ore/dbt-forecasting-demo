-- models/audit/audit_invalid_online_retail.sql
-- This model shows the number of rows dropped during staging
-- due to null customer_id, non-positive quantity, or unit_price.

with raw as (
    select * from raw_online_retail
),

invalid as (

    select
        *,
        case when "Customer ID" is null then 'missing_customer_id'
             when Quantity <= 0 then 'invalid_quantity'
             when Price <= 0 then 'invalid_unit_price'
             else null
        end as issue_type
    from raw
    where
        "Customer ID" is null
        or Quantity <= 0
        or Price <= 0

)

select
    issue_type,
    count(*) as num_rows
from invalid
group by issue_type