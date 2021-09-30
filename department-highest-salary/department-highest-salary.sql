# Write your MySQL query statement below

SELECT d.Name as Department, e.Name as Employee, e.Salary as Salary
FROM Employee e LEFT JOIN Department d on d.Id = e.DepartmentId
WHERE (e.DepartmentId,Salary)
IN
(SELECT DepartmentId,max(Salary)
FROM Employee group by DepartmentId)

