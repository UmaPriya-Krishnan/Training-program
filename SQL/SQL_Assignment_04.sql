umapriya.krishnan
11740611

1. select d.Dept_id ,d.Dept_Name,
   case when e.dept_id is null
   then 0
   else sum(emp_sal)
   end as sum_emp_sal
   from dept d left join emp e on d.dept_id=e.dept_id group by d.dept_id;

+---------+-----------+-------------+
| Dept_id | Dept_Name | sum_emp_sal |
+---------+-----------+-------------+
|       1 | IT        |        9000 |
|       2 | ADMIN     |       11000 |
|       4 | HR        |           0 |
+---------+-----------+-------------+
3 rows in set (0.43 sec)

2. select e.Dept_id,
case when d.dept_name is null
then 'Others'
else d.dept_name
end as Dept_name, sum(emp_sal) as 'Salary_sum'
from emp e left join dept d on e.dept_id=d.dept_id group by e.dept_id order by e.dept_id;

+---------+-----------+------------+
| Dept_id | Dept_name | Salary_sum |
+---------+-----------+------------+
|       1 | IT        |       9000 |
|       2 | ADMIN     |      11000 |
|       3 | Others    |       7000 |
+---------+-----------+------------+
3 rows in set (0.01 sec)


3.mysql> SELECT * FROM employee1 WHERE salary >= 2700 AND salary <= 10000;
+--------+----------+------------+--------+
| emp_id | emp_name | manager_id | salary |
+--------+----------+------------+--------+
|      3 | Vinoth   |          1 |   3000 |
|      4 | Abhishek |          2 |   5000 |
|      5 | Divya    |          3 |   6000 |
|      8 | Aarthi   |          4 |   2700 |
+--------+----------+------------+--------+
4 rows in set (0.00 sec)

4. mysql> select e2.emp_id as manager_id, e2.emp_name as manager_name,sum(e1.salary) as sum_emp_sal
    -> from employee1 e1 join employee1 e2 on e1.manager_id=e2.emp_id group by e1.manager_id;
+------------+--------------+-------------+
| manager_id | manager_name | sum_emp_sal |
+------------+--------------+-------------+
|          1 | Vivek        |        5000 |
|          2 | Raj     
     |        5000 |
|          3 | Vinoth       |       10850 |
|          4 | Abhishek     |        2700 |
|          8 | Aarthi       |       11000 |
+------------+--------------+-------------+
5 rows in set (0.10 sec)


5. mysql> select emp_id,substr(emp_name,4) as derv_emp_name from employee2;
+--------+-----------------+
| emp_id | derv_emp_name   |
+--------+-----------------+
|      1 | eshKumar        |
|      2 | ayaRaja         |
|      3 | ishek           |
|      4 | eshKumar        |
|      5 | ayaprakashSingh |
|      6 | yashree         |
+--------+-----------------+
6 rows in set (0.00 sec)

6. mysql> SELECT EMP_ID, SUBSTR(EMP_NAME, INSTR(EMP_NAME, 'h')+1) AS EMP_NAME FROM EMPLOYEE2;
+--------+----------+
| EMP_ID | EMP_NAME |
+--------+----------+
|      1 | Kumar    |
|      2 | ayaRaja  |
|      3 | ishek    |
|      4 | Kumar    |
|      5 | Singh    |
|      6 | ree      |
+--------+----------+
6 rows in set (0.00 sec)


7. mysql> select emp_id,emp_name,salary from employee1 e1 where 1=(select count(distinct salary) from employee1 e2 where e2.salary>e1.salary);
+--------+----------+--------+
| emp_id | emp_name | salary |
+--------+----------+--------+
|      5 | Divya    |   6000 |
+--------+----------+--------+
1 row in set (0.12 sec)

or 


select * from (select emp_id,emp_name,salary, dense_rank()
over(order by salary desc)as a from employee1) b where a=2;
+--------+----------+--------+---+
| emp_id | emp_name | salary | a |
+--------+----------+--------+---+
|      5 | dhivya   |   6000 | 2 |
+--------+----------+--------+---+
1 row in set (0.00 sec)



9. mysql> select * from employee3
    -> where (salary>3000 and dept_name='IT') or (salary>3400 and dept_name='Admin') order by emp_name;
+--------+----------+-----------+--------+
| emp_id | emp_name | dept_name | salary |
+--------+----------+-----------+--------+
|      4 | Abhishek | IT        |   5700 |
|      2 | Raj      | Admin     |   3500 |
+--------+----------+-----------+--------+
2 rows in set (0.03 sec)

10. mysql> SELECT EMP_ID, EMP_NAME, DEPT_NAME, SALARY, INSTR(EMP_NAME, 'J') AS POS FROM EMPLOYEE4 HAVING POS <>0;
+--------+-----------+-----------+--------+------+
| EMP_ID | EMP_NAME  | DEPT_NAME | SALARY | POS  |
+--------+-----------+-----------+--------+------+
|      1 | Rajesh    | IT        |   2000 |    3 |
|      2 | Ajaykumar | Admin     |   3500 |    2 |
|      5 | Balaji    | ITES      |   3000 |    5 |
+--------+-----------+-----------+--------+------+
3 rows in set (0.00 sec) 

OR

mysql> select * from employee4
    -> where emp_name like '%j%';
+--------+-----------+-----------+--------+
| emp_id | emp_name  | dept_name | salary |
+--------+-----------+-----------+--------+
|      1 | Rajesh    | IT        |   2000 |
|      2 | Ajaykumar | Admin     |   3500 |
|      5 | Balaji    | ITES      |   3000 |
+--------+-----------+-----------+--------+
3 rows in set (0.00 sec)

11.mysql> SELECT EMP_ID, EMP_NAME, DEPT_NAME, SALARY FROM EMPLOYEE4 WHERE EMP_NAME LIKE '%J%' OR EMP_NAME LIKE '%N%' OR EMP_NAME LIKE '%M%';
+--------+------------+-----------+--------+
| EMP_ID | EMP_NAME   | DEPT_NAME | SALARY |
+--------+------------+-----------+--------+
|      1 | Rajesh     | IT        |   2000 |
|      2 | Ajaykumar  | Admin     |   3500 |
|      4 | Vivekkumar | IT        |   5700 |
|      5 | Balaji     | ITES      |   3000 |
|      6 | Raveendar  | HR        |   5800 |
|      7 | Poornarao  | Admin     |   3200 |
+--------+------------+-----------+--------+
6 rows in set (0.00 sec)


12.mysql> SELECT * FROM EMPLOYEE4 WHERE EMP_NAME LIKE '%B%' AND EMP_NAME LIKE '%H%' AND EMP_NAME LIKE '%E%';
+--------+----------+-----------+--------+
| emp_id | emp_name | dept_name | salary |
+--------+----------+-----------+--------+
|      3 | Abhishek | HR        |   4800 |
+--------+----------+-----------+--------+
1 row in set (0.00 sec)



8)Fetch emp_id,Emp_name & Salary who is getting top 3 salary
Note : Don’t use top 

mysql> select * from (select emp_id,emp_name,salary, dense_rank()
    -> over(order by salary desc)as a from employee1) b where a<=3;
+--------+----------+--------+---+
| emp_id | emp_name | salary | a |
+--------+----------+--------+---+
|      1 | Vivek    |  11000 | 1 |
|      5 | Divya    |   6000 | 2 |
|      4 | Abhishek |   5000 | 3 |
+--------+----------+--------+---+
3 rows in set (2.35 sec)