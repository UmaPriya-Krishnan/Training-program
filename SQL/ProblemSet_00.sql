1> CREATE TABLE employee(e_id VARCHAR(5),name VARCHAR(20),dep_id VARCHAR(5),salary INT,manager_id varchar(10));
2> CREATE TABLE dept(dep_id VARCHAR(5),dep_name VARCHAR(20),dep_manager VARCHAR(20));
3> go
1> INSERT INTO employee VALUES('A114','Martin Tredeau','D01',54497,'A120');
2>
3>  INSERT INTO employee VALUES('A116','Robin Wayne','D02',20196,'A187');
4>
5>  INSERT INTO employee VALUES('A178','Bruce Wills','D03',66861,'A298');
6>
7>  INSERT INTO employee VALUES('A132','Paul Vincent','D01',94791,'A120');
8>
9>  INSERT INTO employee VALUES('A198','Tom Hanks','D02',16879,'A187');
10>
11>  INSERT INTO employee VALUES('A120','Tim Archer','D01',48834,'A298');
12>
13>  INSERT INTO employee VALUES('A143','Brad Michael','D01',24488,'A120');
14>
15>  INSERT INTO employee VALUES('A187','Adam Justin','D02',80543,'A298');
16>
17>  INSERT INTO employee VALUES('A121','Stuart William','D02',78629,'A187');
18>
19>  INSERT INTO employee VALUES('A187','Robert Swift','D04',27700,'A298');
20>
21>  INSERT INTO employee VALUES('A176','Edward Cane','D01',89176,'A120');
22>
23>  INSERT INTO employee VALUES('A142','Tara Cummings','D04',99475,'A187');
24>
25>  INSERT INTO employee VALUES('A130','Vanessa Pary','D04',28565,'A187');
26>
27>  INSERT INTO employee VALUES('A128','Adam Wayne','D05',94324,'A165');
28>
29>  INSERT INTO employee VALUES('A129','Joseph Angelin','D05',44280,'A165');
30>
31>  INSERT INTO employee VALUES('A165','Natasha Stevens','D05',31377,'A298');
32>
33>  INSERT INTO employee VALUES('A165','Natasha Stevens','D05',31377,'A298');
34>
35>  INSERT INTO employee VALUES('A194','Harolld Stevens','D02',32166,'A187');
36>
37>  INSERT INTO employee VALUES('A133','Steve Michelos','D02',61215,'A187');
38>
39>  INSERT INTO employee VALUES('A156','Nick Martin','D03',50174,'A178');
40>
41>  INSERT INTO dept VALUES('D01','Health','Tim Archer');
42>
43>  INSERT INTO dept VALUES('D02','Communications','Adam Justin');
44>
45>  INSERT INTO dept VALUES('D03','Product','Bruce Wills');
46>
47>  INSERT INTO dept VALUES('D04','Insurance','Robert Swift');
48>
49>  INSERT INTO dept VALUES('D05','Finance','Natasha Stevens');
50>
51> go

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

1> select * from employee
2> select * from dept
3> go
e_id  name                 dep_id salary      manager_id
----- -------------------- ------ ----------- ----------
A114  Martin Tredeau       D01          54497 A120
A116  Robin Wayne          D02          20196 A187
A178  Bruce Wills          D03          66861 A298
A132  Paul Vincent         D01          94791 A120
A198  Tom Hanks            D02          16879 A187
A120  Tim Archer           D01          48834 A298
A143  Brad Michael         D01          24488 A120
A187  Adam Justin          D02          80543 A298
A121  Stuart William       D02          78629 A187
A187  Robert Swift         D04          27700 A298
A176  Edward Cane          D01          89176 A120
A142  Tara Cummings        D04          99475 A187
A130  Vanessa Pary         D04          28565 A187
A128  Adam Wayne           D05          94324 A165
A129  Joseph Angelin       D05          44280 A165
A165  Natasha Stevens      D05          31377 A298
A165  Natasha Stevens      D05          31377 A298
A194  Harolld Stevens      D02          32166 A187
A133  Steve Michelos       D02          61215 A187
A156  Nick Martin          D03          50174 A178

(20 rows affected)
dep_id dep_name             dep_manager
------ -------------------- --------------------
D01    Health               Tim Archer
D02    Communications       Adam Justin
D03    Product              Bruce Wills
D04    Insurance            Robert Swift
D05    Finance              Natasha Stevens

(5 rows affected)


1)Select the Employee with the top three salaries

SELECT TOP 3 name, salary from employee order by salary desc
o/p:
name                 salary
-------------------- -----------
Tara Cummings              99475
Paul Vincent               94791
Adam Wayne                 943241)Select the Employee with the top three salaries

SELECT TOP 3 name, salary from employee order by salary desc
o/p:
name                 salary
-------------------- -----------
Tara Cummings              99475
Paul Vincent               94791
Adam Wayne                 94324

************************************************************************************************************

2)Select the Employee with the least salary

SELECT MIN(salary) as min_salary FROM employee
o/p:
min_salary
-----------
      16879

************************************************************************************************************

3)Select the Employee who does not have a manager in the department table

SELECT name FROM employee AS E INNER JOIN dept AS D ON D.dep_id = E.dep_id WHERE D.dep_manager = 'NULL'
or
 SELECT name FROM employee WHERE dep_id NOT IN (SELECT dep_id FROM dept);
O/P:
name
-------------------- 
--(empty)

*************************************************************************************************************
4)Select the Employee who is also a Manager

SELECT name FROM employee AS E INNER JOIN dept AS D ON D.dep_id = E.dep_id WHERE E.name = D.dep_manager

or 
SELECT name FROM employee , dept WHERE name = dep_manager ;
O/P:
name
--------------------
Bruce Wills
Tim Archer
Robert Swift
Natasha Stevens

****************************************************************************************************************

5)Select the Empolyee who is a Manager and has least salary

 SELECT min(salary) FROM employee WHERE name in ( select dep_manager from dept ) ;
o/p:
min_sal
-----------
      27700

***************************************************************************************************************************

6)Select the total number of Employees in Communications departments

SELECT COUNT(name)as count FROM employee AS E INNER JOIN dept AS D ON D.dep_id = E.dep_id  WHERE dep_name = 'COMMUNICATIONS'
o/p:
COUNT
-----------
          6
****************************************************************************************************************************************
7)Select the Employee in Finance Department who has the top salary

SELECT TOP 1 name,salary  FROM employee AS E INNER JOIN dept AS D ON D.dep_id = E.dep_id WHERE dep_name = 'FINANCE' order by salary desc
o/p:
name                 salary
-------------------- -----------
Adam Wayne                 94324

****************************************************************************************************************************************
8)Select the Employee in product depatment who has the least salary

 SELECT TOP 1 name, salary FROM employee AS E INNER JOIN dept AS D ON D.dep_id = E.dep_id WHERE dep_name = 'PRODUCT' ORDER BY  salary
o/p:
name                 salary
-------------------- -----------
Nick Martin                50174

***********************************************************************************************************************************

9. Select the count of employees in health with maximum salary

1> select count(name) as count , salary from employee join dept on employee.dep_id=dept.dep_id where salary = ( select max(salary) from employee,dept where employee.dep_id=dept.dep_id and dept.dep_name = 'Health' ) group by salary;
2> go
count       salary
----------- -----------
          1       94791

(1 rows affected)

***********************************************************************************************************************
10)Select the Employees who report to Natasha Stevens

SELECT name FROM employee AS E INNER JOIN dept AS D ON D.dep_id = E.dep_id WHERE D.dep_manager ='NATASHA STEVENS';
O/P:
name
--------------------
Adam Wayne
Joseph Angelin
Natasha Stevens

***************************************************************************************************************************************************
11)Display the Employee name,Employee count,Dep name,Dept manager in the Health department

SELECT COUNT(name) AS count name, dep_name, dep_manager FROM employee AS E LEFT OUTER JOIN dept AS D ON D.dep_id = E.dep_id WHERE dep_name = 'HEALTH'
O/P:
name                 dep_name             dep_manager
-------------------- -------------------- --------------------
Martin Tredeau       Health               Tim Archer
Paul Vincent         Health               Tim Archer
Tim Archer           Health               Tim Archer
Brad Michael         Health               Tim Archer
Edward Cane          Health               Tim Archer

***********************************************************************************************************************************

12)Display the Department id,Employee ids and Manager ids for the Communications department

SELECT E.dep_id, e_id, manager_id FROM employee AS E INNER JOIN dept AS D ON D.dep_id = E.dep_id WHERE dep_name = 'COMMUNICATIONS'
O/P:
dep_id e_id  manager_id
------ ----- ----------
D02    A116  A187
D02    A198  A187
D02    A187  A298
D02    A121  A187
D02    A194  A187
D02    A133  A187
***********************************************************************************************************************************

13. Select the average expenses of each department with dept_id and dept_name.

1> select E.dep_id, D.dep_name, avg(salary) from employee as E join dept as D on E.dep_id = D.dep_id group by E.dep_id, D.dep_name;
2> go
dep_id dep_name
------ ---------------------------------------- -----------
D01    Health                                         62357
D02    Communications                                 48271
D03    Product                                        58517
D04    Insurance                                      51913
D05    Finance                                        56660

(5 rows affected)

***********************************************************************************************************************************
14)Select the total expense for the department finance

SELECT SUM(salary) AS total_expense FROM employee AS E INNER JOIN dept AS D on E.dep_id = D.dep_id WHERE dep_name = 'FINANCE'
O/P:
total_expense
-------------
       169981
***********************************************************************************************************************************

15)Select the department which spends the least with Dept id and Dept manager name

1> select E.dep_id ,dep_manager ,dep_name from employee as E join dept as D on E.dep_id=D.dep_id where salary in ( select min(employee.salary) from employee) and E.dep_id=D.dep_id;
2> go

o/p:

dep_id dep_manager          dep_name
------ -------------------- ----------------------------------------
D02    Adam Justin         Communications

(1 rows affected)

*************************************************************************************************************************************
16)Select the count of Employees in each department

 SELECT COUNT(employee.e_id) AS count, dept.dep_name FROM employee, dept WHERE employee.dep_id=dept.dep_id GROUP BY dept.dep_name;
o/p:
count       dep_name
----------- --------------------
          6 Communications
          3 Finance
          5 Health
          3 Insurance
          2 Product

**************************************************************************************************************************************
17)Select the count of Employees in each department having salary <10000

SELECT COUNT(employee.e_id) AS count, dept.dep_name FROM employee, dept WHERE employee.dep_id=dept.dep_id AND employee.salary < 10000 GROUP BY dept.dep_name;
o/p:
count       dep_name
----------- --------------------

****************************************************************************************************************************************

18)Select the total number of Employees in Dept id D04

SELECT count(e_id) AS count FROM employee where dep_id='D04';
o/p:
count
-----------
          3
*****************************************************************************************************************************************
19)Select all department details of the Department with Maximum Employees

SELECT max(e_id),dep_name FROM (SELECT count(e_id) e_id FROM employee group by dep_id)as d, dept;

o/p:

******************************************************************************************************************************************
20)Select the Employees who has Tim Cook as their manager

SELECT name FROM employee as E INNER JOIN dept as D on E.dep_id = D.dep_id where dep_manager = 'Tim Cook'
O/P:
name
--------------------
(EMPTY)

