BEGIN;

\echo Create import table...

CREATE TEMPORARY TABLE conditional_grants_upsert
(
        demarcation_code TEXT,
        period_code TEXT,
        grant_code TEXT,
        amount DECIMAL
) ON COMMIT DROP;

\echo Read data...

\copy conditional_grants_upsert (demarcation_code, period_code, grant_code, amount) FROM '/home/jdb/proj/code4sa/municipal_finance/datasets/2017q1/grants_2017q1_acrmun.csv' DELIMITER ',' CSV HEADER;

\echo Delete demarcation_code-period_code pairs that are in the update

DELETE FROM conditional_grants_facts f WHERE EXISTS (
        SELECT 1 FROM conditional_grants_upsert i
        WHERE f.demarcation_code = i.demarcation_code
        AND f.period_code = i.period_code
        LIMIT 1
    );

\echo Insert new values...

INSERT INTO conditional_grants_facts
(
    demarcation_code,
    period_code,
    grant_code,
    amount,
    financial_year,
    amount_type_code,
    period_length,
    financial_period
)
SELECT demarcation_code,
       period_code,
       grant_code,
       amount,
       cast(left(period_code, 4) as int),
       case when substr(period_code, 5) in ('IBY1', 'IBY2', 'ADJB', 'ORGB', 'AUDA', 'PAUD')
           then substr(period_code, 5)
           else 'ACT'
       end,
       case when substr(period_code, 5, 3) not similar to 'M\d{2}'
            then 'year'
            else 'month'
       end,
       case when substr(period_code, 5, 3) similar to 'M\d{2}'
            then cast(right(period_code, 2) as int)
            else cast(left(period_code, 4) as int)
       end
FROM conditional_grants_upsert i;

COMMIT;
