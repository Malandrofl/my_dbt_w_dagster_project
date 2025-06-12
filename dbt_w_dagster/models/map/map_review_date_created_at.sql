{{ config(
  materialized = 'view'
) }}
WITH
l AS (
    SELECT
        *
    FROM
        {{  ref('dim_listings_cleansed')}}
),
h AS (
    SELECT *
    FROM  {{ ref('fct_reviews') }}
)

SELECT
    l.created_at,
    h.review_date,
FROM l
LEFT JOIN h ON (h.listing_id = l.listing_id)
