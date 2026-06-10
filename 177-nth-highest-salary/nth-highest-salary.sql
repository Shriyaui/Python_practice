CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE offset_val INT;
  SET offset_val = N - 1;
  RETURN (
      SELECT IFNULL(
          (SELECT DISTINCT salary 
           FROM Employee 
           ORDER BY salary DESC 
           LIMIT 1 OFFSET offset_val),
          NULL
      )
  );
END