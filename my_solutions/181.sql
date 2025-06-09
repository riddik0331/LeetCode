# Write your MySQL query statement below
SELECT name as Employee
FROM Employee as empl
WHERE salary > (
    SELECT salary FROM Employee as e
    WHERE e.id = empl.managerId
)
