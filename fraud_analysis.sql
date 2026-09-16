-- 1. Total number of transactions
SELECT COUNT(*) AS total_transactions
FROM transactions;

-- 2. Number of fraudulent transactions
SELECT COUNT(*) AS fraud_transactions
FROM transactions
WHERE Class = 1;

-- 3. Number of normal transactions
SELECT COUNT(*) AS normal_transactions
FROM transactions
WHERE Class = 0;

-- 4. Fraud rate
SELECT
    AVG(CASE WHEN Class = 1 THEN 1.0 ELSE 0.0 END) AS fraud_rate
FROM transactions;

-- 5. Average transaction amount
SELECT
    AVG(Amount) AS average_transaction_amount
FROM transactions;

-- 6. Average amount by transaction class
SELECT
    Class,
    COUNT(*) AS transaction_count,
    AVG(Amount) AS average_amount
FROM transactions
GROUP BY Class;

-- 7. Maximum fraudulent transaction amount
SELECT
    MAX(Amount) AS maximum_fraud_amount
FROM transactions
WHERE Class = 1;