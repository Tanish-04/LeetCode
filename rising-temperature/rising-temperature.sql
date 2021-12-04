# Write your MySQL query statement below
SELECT w1.id
FROM WEATHER w1, WEATHER w2
WHERE w1.temperature > w2.temperature
AND datediff(w1.recordDate,w2.recordDate) = 1
