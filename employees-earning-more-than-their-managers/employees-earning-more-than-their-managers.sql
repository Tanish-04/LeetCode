# Write your MySQL query statement below

SELECT e.name as Employee from Employee e, Employee m
where e.managerId = m.Id
and e.salary > m.salary
