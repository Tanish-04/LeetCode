# Write your MySQL query statement below

SELECT class
FROM courses
group by class
having count(distinct student) >= 5