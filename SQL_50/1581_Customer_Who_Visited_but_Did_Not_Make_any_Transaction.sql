# https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/submissions/1909483143/?envType=study-plan-v2&envId=top-sql-50
# Write your MySQL query statement below
SELECT v.customer_id, count(*) as count_no_trans
FROM Visits v
left JOIN Transactions t
ON v.visit_id=t.visit_id
WHERE t.visit_id is null
group by(v.customer_id)
