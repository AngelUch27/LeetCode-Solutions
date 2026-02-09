# 197. Rising Temperature
#https://leetcode.com/problems/rising-temperature/?envType=study-plan-v2&envId=top-sql-50
# Write your MySQL query statement below
SELECT w2.id
from Weather w1
JOIN Weather w2
ON w2.recordDate = DATE_ADD(w1.recordDate, INTERVAL 1 DAY)
WHERE w2.temperature>w1.temperature;
