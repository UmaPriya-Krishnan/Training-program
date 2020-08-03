umapriya.krishnan
11740611
		 						
1. select e.emp_id, e.emp_name, 
CASE when d.desc_name is null then 'others'
when d.desc_name is not null and d.role_typ = 'lead' then 'TEAM_LEAD'
else d.desc_name end as desc_name,
CASE when p.place_desc is null then 'Others'
else p.place_desc end as place_desc,
CASE when pr.proj_name is null then 'others'
else pr.proj_name end as proj_name from employee e left join designation d 
on e.desc_id = d.desc_id  left join place p on e.place_id = p.place_id  left join
project pr on e.proj_id = pr.proj_id order by emp_id; 

+--------+---------------+---------------------+------------+-----------------+
| emp_id | emp_name      | desc_name           | place_desc | proj_name       |
+--------+---------------+---------------------+------------+-----------------+
|      1 | Vijaykumar    | ASE                 | Chennai    | Pepsi           |
|      2 | Raja          | SE                  | Hyderabad  | Microsoft       |
|      3 | Abhisheksingh | ASE                 | Mexico     | Amazon          |
|      4 | Santosh       | SSE                 | Bangalore  | Cigna           |
|      5 | Kribakaran    | SE                  | Hyderabad  | ASG             |
|      6 | Divya         | TEAM_LEAD           | USA        | Pepsi           |
|      7 | Suganya       | ASE                 | Hyderabad  | Microsoft       |
|      8 | Shalini       | SE                  | Bangalore  | ASG             |
|      9 | Avantika      | SSE                 | Chennai    | Amazon          |
|     10 | Ajay          | TEAM_LEAD           | Others     | UNKNOWN PROJECT |
|     11 | Tamilselvan   | UNKNOWN DESIGNATION | Others     | UNKNOWN PROJECT |
|     12 | Vinodha       | UNKNOWN DESIGNATION | Others     | UNKNOWN PROJECT |
|     13 | Karthick      | UNKNOWN DESIGNATION | USA        | ASG             |
|     14 | Sanjay        | UNKNOWN DESIGNATION | Others     | Amazon          |
|     15 | Meera         | UNKNOWN DESIGNATION | Others     | UNKNOWN PROJECT |
+--------+---------------+---------------------+------------+-----------------+
15 rows in set (0.94 sec)


2. select e.emp_id, e.emp_name, case when
d.role_typ = 'DEVELOPER' and p.place_typ = 'OFFSHORE'
then 'TEAMMEMBER'
WHEN d.role_typ = 'DEVELOPER' and p.place_typ = 'NEARSHORE'
then 'TEAMLEAD'
WHEN d.role_typ = 'DEVELOPER' and p.place_typ = 'ONSHORE'
then 'BA'
WHEN d.role_typ = 'LEAD' and p.place_typ = 'ONSHORE'
then 'SCRUMMASTER'
WHEN  d.role_typ is not null or p.place_typ is not null 
then 'CONTACTOR'
else 'SHADOW' end as 'project_role'
from employee as e left join designation d on e.desc_id = d.desc_id left  join place p on e.place_id = p.place_id 
left join project pr on e.proj_id = pr.proj_id;

3.select
    CASE WHEN d.ROLE_TYP='DEVELOPER' THEN D.ROLE_TYP ELSE 'OTHERS' END AS DERV_ROLE_TYP,
    CASE WHEN d.ROLE_TYP ='DEVELOPER'  THEN p.PLACE_DESC ELSE 'OTHERS' END AS DERV_PLACE_DESC ,
    CASE WHEN d.ROLE_TYP='DEVELOPER' THEN pr.PROJ_NAME ELSE 'OTHERS'  END AS DERV_PROJ_DESC,
    count(e.emp_id) AS COUNT from Employee as e
    left  join Designation as d
    on e.DESC_ID=d.DESC_ID and d.ROLE_TYP='DEVELOPER'
    left  join Place as p
    on e.PLACE_ID=p.PLACE_ID
    left  join Project as pr  on
    e.PROJ_ID=pr.PROJ_ID
    group by DERV_ROLE_TYP,DERV_PLACE_DESC,DERV_PROJ_DESC ORDER BY COUNT;
	
	+---------------+-----------------+----------------+-------+
| DERV_ROLE_TYP | DERV_PLACE_DESC | DERV_PROJ_DESC | COUNT |
+---------------+-----------------+----------------+-------+
| DEVELOPER     | Chennai         | Pepsi          |     1 |
| DEVELOPER     | Mexico          | Amazon         |     1 |
| DEVELOPER     | Bangalore       | Cigna          |     1 |
| DEVELOPER     | Hyderabad       | ASG            |     1 |
| DEVELOPER     | Bangalore       | ASG            |     1 |
| DEVELOPER     | Chennai         | Amazon         |     1 |
| DEVELOPER     | Hyderabad       | Microsoft      |     2 |
| OTHERS        | OTHERS          | OTHERS         |     7 |
+---------------+-----------------+----------------+-------+
8 rows in set (0.00 sec)

4. mysql> select
    -> COALESCE(E.EMP_NAME,'OTHERS') AS DERV_EMP_NAME,
    -> COALESCE(D.DESC_NAME,'OTHERS') AS DERV_DESC_NAME,
    -> COALESCE(p.PLACE_DESC,'OTHERS') AS DERV_PLACE_DESC ,
    -> COALESCE(pr.PROJ_NAME,'OTHERS')  AS DERV_PROJ_DESC
    -> from Employee as e
    -> full outer join Designation d on e.DESC_ID=d.DESC_ID
    -> full outer join Place p on e.PLACE_ID=p.PLACE_ID
    -> full outer join Project pr on e.PROJ_ID=pr.PROJ_ID;
	
	
	
5. SELECT s.salesman_Name, c.cust_name, s.city as salesman_city, c.city as customer_city 
from customer c join salesman s  on c.salesman_id = s.salesman_id where s.city <> c.city;

+---------------+-----------+---------------+---------------+
| salesman_Name | cust_name | salesman_city | customer_city |
+---------------+-----------+---------------+---------------+
| Raju          | Ricky     | Hyderabad     | Chennai       |
| Srinath       | Amaran    | Mumbai        | Chennai       |
+---------------+-----------+---------------+---------------+
2 rows in set (0.66 sec)


6. select s.salesman_Name, s.salesman_id, s.city, s.monthly_target, sum(c.purchased_amount ) as amount_purchased_by_customer
from customer c join salesman s on c.salesman_id = s.salesman_id
group by s.salesman_id  having amount_purchased_by_customer >= s.Monthly_Target;

+---------------+-------------+-----------+----------------+------------------------------+
| salesman_Name | salesman_id | city      | monthly_target | amount_purchased_by_customer |
+---------------+-------------+-----------+----------------+------------------------------+
| John          |           1 | Chennai   |          10000 |                        10000 |
| Raju          |           3 | Hyderabad |          21000 |                        23000 |
| Srinath       |           4 | Mumbai    |           9000 |                         9000 |
| Vijay         |           5 | Chennai   |           4000 |                         5000 |
+---------------+-------------+-----------+----------------+------------------------------+
4 rows in set (0.04 sec)


7. mysql> select * from
    -> (select cust_name,city,priority_num,purchased_amount,dense_rank() over(partition by priority_num order by purchased_amount desc) rnk from customer) as a
    -> where a.rnk IN (1,2);
+-----------+-----------+--------------+------------------+-----+
| cust_name | city      | priority_num | purchased_amount | rnk |
+-----------+-----------+--------------+------------------+-----+
| James     | Chennai   |            1 |            10000 |   1 |
| Ricky     | Chennai   |            1 |             8000 |   2 |
| Ramu      | Bangalore |            1 |             8000 |   2 |
| Jyothi    | Hyderabad |            2 |             9000 |   1 |
| Akilan    | Hyderabad |            2 |             6000 |   2 |
| Dinesh    | Mumbai    |            2 |             6000 |   2 |
+-----------+-----------+--------------+------------------+-----+
6 rows in set (0.10 sec)


8. select  s.Salesman_Name,s.City,s.Monthly_Target,case when c.Purchased_Amount is null then 0
else sum(c.Purchased_Amount) end as Amount_purchase_by_Customer
from  Customer as c   right join Salesman as s on c.Salesman_id=s.Salesman_id
group by s.Salesman_Name,s.City,s.Monthly_Target having Amount_purchase_by_Customer<
(select avg(s.Monthly_Target) as avg_monthly_target from Salesman as s );

+---------------+-----------+----------------+-----------------------------+
| Salesman_Name | City      | Monthly_Target | Amount_purchase_by_Customer |
+---------------+-----------+----------------+-----------------------------+
| John          | Chennai   |          10000 |                       10000 |
| Abraham       | Bangalore |          21000 |                        8000 |
| Srinath       | Mumbai    |           9000 |                        9000 |
| Vijay         | Chennai   |           4000 |                        5000 |
| Balaji        | Hyderabad |          15000 |                           0 |
+---------------+-----------+----------------+-----------------------------+
5 rows in set (0.31 sec)

9.mysql>  select mgr_salesman_name,emp_salesman_name,mgr_Monthly_Target,emp_Amount_purchase_by_Customer
    -> from
    -> (select distinct mgr.salesman_id as mgr_salesman_id, mgr.salesman_name as mgr_salesman_name,
    -> emp.salesman_name as emp_salesman_name, mgr.monthly_target as mgr_Monthly_Target,
    -> sum(c.purchased_amount) over (partition by mgr.salesman_id) as mgr_Amount_purchase_by_Customer ,
    -> sum(c.purchased_amount) over (partition by emp.salesman_id) as emp_Amount_purchase_by_Customer
    -> from salesman emp join salesman mgr on emp.salesman_id = mgr.salesman_id inner join customer c
    -> on c.salesman_id=emp.salesman_id) tmp where mgr_monthly_target <= mgr_Amount_purchase_by_Customer;
+-------------------+-------------------+--------------------+---------------------------------+
| mgr_salesman_name | emp_salesman_name | mgr_Monthly_Target | emp_Amount_purchase_by_Customer |
+-------------------+-------------------+--------------------+---------------------------------+
| John              | John              |              10000 |                           10000 |
| Raju              | Raju              |              23000 |                           23000 |
| Srinath           | Srinath           |               9000 |                            9000 |
| Vijay             | Vijay             |               5000 |                            5000 |
+-------------------+-------------------+--------------------+---------------------------------+
4 rows in set (1.14 sec)

10. mysql> select Student_name,city_name,Class from(
    -> select s.Student_name,c.city_name,cl.Class,row_number() over (partition by s.Student_name order by sd.Start_date) as rn_student_date from Student as s
    -> inner join Student_details as sd on
    -> s.Student_Detail_id=sd.Student_Detail_id inner join City as c on sd.City_Id=c.City_Id
    -> inner join Class as cl on sd.Class_Id=cl.Class_Id)as a where rn_student_date=1;
+--------------+-----------+-------+
| Student_name | city_name | Class |
+--------------+-----------+-------+
| Ajay         | Chennai   | 11th  |
| Gopi         | Bangalore | 10th  |
| Kalai        | Chennai   | 11th  |
| Ramesh       | Bangalore | 10th  |
| Shriram      | Bangalore | 10th  |
| Vinoth       | Bangalore | 12th  |
+--------------+-----------+-------+
6 rows in set (2.40 sec)

11. select Student_name,City_name,class as class_name, Classroom_num from student  a inner join
student_details b
on a.Student_Detail_Id=b.Student_Detail_Id
and b.start_date <= current_date and b.end_date >= current_date
inner join  city c on b.City_id=c.City_id
inner join class d on b.Class_id=d.Class_id
and d.start_date <= current_date and d.end_date >= current_date;
+--------------+-----------+------------+---------------+
| Student_name | City_name | class_name | Classroom_num |
+--------------+-----------+------------+---------------+
| Ajay         | Chennai   | 12th       |           371 |
| Ramesh       | Mumbai    | 11th       |           320 |
| Shriram      | Chennai   | 12th       |           371 |
| Gopi         | Mumbai    | 11th       |           320 |
| Kalai        | Chennai   | 11th       |           320 |
| Vinoth       | Bangalore | 12th       |           371 |
+--------------+-----------+------------+---------------+
6 rows in set (0.08 sec)

12. select distinct a.Student_name from Student as a
join Student_details as b on
a.Student_Detail_id=b.Student_Detail_id join City as c on b.City_Id=c.City_Id
join Class as d on b.Class_Id=d.Class_Id where c.city_name='Chennai' or d.Classroom_num in(301,310,320); 
 
+--------------+
| Student_name |
+--------------+
| Ajay         |
| Ramesh       |
| Shriram      |
| Gopi         |
| Kalai        |
+--------------+
5 rows in set (0.00 sec)


13. select substr(cust_name,3,length(cust_name)-4) as derv_name from customer1;

+--------------+
| derv_name    |
+--------------+
| mesMart      |
| ckAda        |
| manuj        |
| othiMahaling |
| aranJot      |
| ilanBa       |
| unKum        |
| neshKum      |
+--------------+
8 rows in set (0.19 sec)

14. mysql> select cust_name,case when length(cust_name)>0 then cust_name else 'NO 2nd occurence' end as cust_name
 from(select substring((substring(cust_name,1,length(cust_name)-1)),locate('a',cust_name,(locate('a',cust_name)+1)))
 as cust_name from customer1)cust;
+------------------+
| cust_name        |
+------------------+
| arti             |
| am               |
| anuja            |
| alinga           |
| aranJoth         |
| anBal            |
| a                |
| NO 2nd occurence |
+------------------+
8 rows in set (0.00 sec)


15. select cust_name from customer1 where cust_name like '%A%' or cust_name like'%U%' or cust_name like '%R%';

+------------------+
| cust_name        |
+------------------+
| JamesMartin      |
| RickAdams        |
| Ramanujam        |
| JyothiMahalingam |
| AmaranJothi      |
| AkilanBala       |
| ArunKumar        |
| DineshKumar      |
+------------------+
8 rows in set (0.10 sec)

