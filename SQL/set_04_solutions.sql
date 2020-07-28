1. Find the names of all students who are friends with someone named Gabriel. (1 point possible)

mysql> select name from highschooler h join friend f on h.id=f.id1 where id2 in 
(select id from highschooler where name="Gabriel");
+-----------+
| name      |
+-----------+
| Jordan    |
| Cassandra |
| Andrew    |
| Alexis    |
| Jessica   |
+-----------+
5 rows in set (0.00 sec)


2. For every student who likes someone 2 or more grades younger than themselves,
 return that students name and grade, and the name and grade of the student they like. (1 point possible)

mysql> select h1.name, h1.grade, h2.name, h2.grade from highschooler as h1 join likes as l on l.id1 = h1.id join highschooler as h2 on h2.id = l.id2;
+-----------+-------+-----------+-------+
| name      | grade | name      | grade |
+-----------+-------+-----------+-------+
| Cassandra |     9 | Gabriel   |     9 |
| Gabriel   |     9 | Cassandra |     9 |
| Andrew    |    10 | Cassandra |     9 |
| John      |    12 | Haley     |    10 |
| Brittany  |    10 | Kris      |    10 |
| Alexis    |    11 | Kris      |    10 |
| Gabriel   |    11 | Alexis    |    11 |
| Kyle      |    12 | Jessica   |    11 |
| Austin    |    11 | Jordan    |    12 |
| Jessica   |    11 | Kyle      |    12 |
+-----------+-------+-----------+-------+
10 rows in set (0.00 sec)

3. For every pair of students who both like each other, return the name and grade of both students. Include each pair only once, with the two names in alphabetical order. (1 point possible)

mysql> select l1.id1,l2.id2,h1.name,h2.name from likes l1 join likes l2 on l1.id1=l2.id2 and l2.id1=l1.id2 join highschooler h1 on l1.id1=h1.id join highschooler h2 on l2.id1=h2.id where h1.name>h2.name order by h1.name;
+------+------+---------+-----------+
| id1  | id2  | name    | name      |
+------+------+---------+-----------+
| 1689 | 1689 | Gabriel | Cassandra |
| 1934 | 1934 | Kyle    | Jessica   |
+------+------+---------+-----------+
2 rows in set (0.00 sec)

4. Find all students who do not appear in the Likes table (as a student who likes or is liked) and return their names and grades. Sort by grade, then by name within each grade. (1 point possible)

mysql> select id,name,grade from highschooler where id not in(select id1 from likes) or id not in(select id2 from likes) order by grade,name;
+------+----------+-------+
| id   | name     | grade |
+------+----------+-------+
| 1510 | Jordan   |     9 |
| 1381 | Tiffany  |     9 |
| 1782 | Andrew   |    10 |
| 1641 | Brittany |    10 |
| 1101 | Haley    |    10 |
| 1468 | Kris     |    10 |
| 1316 | Austin   |    11 |
| 1911 | Gabriel  |    11 |
| 1025 | John     |    12 |
| 1304 | Jordan   |    12 |
| 1661 | Logan    |    12 |
+------+----------+-------+
11 rows in set (0.01 sec)

6. Find names and grades of students who only have friends in the same grade. Return the result sorted by grade, then by name within each grade. (1 point possible)

mysql> select f.id1,h1.name,h1.grade,f.id2,h2.name,h2.grade from friend f join highschooler h1 on f.id1=h1.id  join highschooler h2 on f.id2=h2.id and h1.grade=h2.grade         order by h1.name,h2.name,h1.grade,h2.grade;
+------+-----------+-------+------+-----------+-------+
| id1  | name      | grade | id2  | name      | grade |
+------+-----------+-------+------+-----------+-------+
| 1247 | Alexis    |    11 | 1911 | Gabriel   |    11 |
| 1247 | Alexis    |    11 | 1501 | Jessica   |    11 |
| 1782 | Andrew    |    10 | 1468 | Kris      |    10 |
| 1641 | Brittany  |    10 | 1101 | Haley     |    10 |
| 1641 | Brittany  |    10 | 1468 | Kris      |    10 |
| 1709 | Cassandra |     9 | 1689 | Gabriel   |     9 |
| 1911 | Gabriel   |    11 | 1247 | Alexis    |    11 |
| 1689 | Gabriel   |     9 | 1709 | Cassandra |     9 |
| 1911 | Gabriel   |    11 | 1501 | Jessica   |    11 |
| 1689 | Gabriel   |     9 | 1510 | Jordan    |     9 |
| 1101 | Haley     |    10 | 1641 | Brittany  |    10 |
| 1101 | Haley     |    10 | 1468 | Kris      |    10 |
| 1501 | Jessica   |    11 | 1247 | Alexis    |    11 |
| 1501 | Jessica   |    11 | 1911 | Gabriel   |    11 |
| 1025 | John      |    12 | 1661 | Logan     |    12 |
| 1510 | Jordan    |     9 | 1689 | Gabriel   |     9 |
| 1304 | Jordan    |    12 | 1934 | Kyle      |    12 |
| 1304 | Jordan    |    12 | 1661 | Logan     |    12 |
| 1510 | Jordan    |     9 | 1381 | Tiffany   |     9 |
| 1468 | Kris      |    10 | 1782 | Andrew    |    10 |
| 1468 | Kris      |    10 | 1641 | Brittany  |    10 |
| 1468 | Kris      |    10 | 1101 | Haley     |    10 |
| 1934 | Kyle      |    12 | 1304 | Jordan    |    12 |
| 1661 | Logan     |    12 | 1025 | John      |    12 |
| 1661 | Logan     |    12 | 1304 | Jordan    |    12 |
| 1381 | Tiffany   |     9 | 1510 | Jordan    |     9 |
+------+-----------+-------+------+-----------+-------+
26 rows in set (0.00 sec)

7. For each student A who likes a student B where the two are not friends, find if they have a friend C in common (who can introduce them!). For all such trios, return the name and grade of A, B, and C. (1 point possible)

mysql> select h1.name,h1.grade,h2.name,h2.grade,h3.name,h3.grade from likes l left join friend f on l.id1=f.id1 and l.id2=f.id2 join friend f1 on l.id1=f1.id1 join friend f2 on l.id2=f2.id1 join highschooler h1 on l.id1=h1.id join highschooler h2 on l.id2=h2.id join highschooler h3 on f1.id2=h3.id where f.id1 is null and f.id2 is null and f1.id2=f2.id2;
+--------+-------+-----------+-------+---------+-------+
| name   | grade | name      | grade | name    | grade |
+--------+-------+-----------+-------+---------+-------+
| Andrew |    10 | Cassandra |     9 | Gabriel |     9 |
| Austin |    11 | Jordan    |    12 | Andrew  |    10 |
| Austin |    11 | Jordan    |    12 | Kyle    |    12 |
+--------+-------+-----------+-------+---------+-------+
3 rows in set (0.00 sec)

8. Find the difference between the number of students in the school and the number of different first names. (1 point possible)

mysql> select count(name)-count(distinct name) as diff from highschooler;
+------+
| diff |
+------+
|    2 |
+------+
1 row in set (0.00 sec)

9. Find the name and grade of all students who are liked by more than one other student. (1 point possible)

mysql> select l.id2,h.name,h.grade,count(*) from likes l join highschooler h on l.id2=h.id group by id2 having count(*)>1;
+------+-----------+-------+----------+
| id2  | name      | grade | count(*) |
+------+-----------+-------+----------+
| 1709 | Cassandra |     9 |        2 |
| 1468 | Kris      |    10 |        2 |
+------+-----------+-------+----------+
2 rows in set (0.00 sec)

10. For every situation where student A likes student B, but student B likes a different student C, return the names and grades of A, B, and C. (1 point possible)

mysql> select h1.name,h1.grade,h2.name,h2.grade,h3.name,h3.grade from likes l1 join likes l2 on l1.id2=l2.id1 and l1.id1<>l2.id2 join highschooler h1 on l1.id1=h1.id join highschooler h2 on l1.id2=h2.id join highschooler h3 on l2.id2=h3.id;
+---------+-------+-----------+-------+---------+-------+
| name    | grade | name      | grade | name    | grade |
+---------+-------+-----------+-------+---------+-------+
| Andrew  |    10 | Cassandra |     9 | Gabriel |     9 |
| Gabriel |    11 | Alexis    |    11 | Kris    |    10 |
+---------+-------+-----------+-------+---------+-------+
2 rows in set (0.00 sec)

11. Find those students for whom all of their friends are in different grades from themselves. Return the students names and grades.(1 point possible)

mysql>  select f.id1,h1.name,h1.grade,f.id2,h2.name,h2.grade from friend f join highschooler h1 on f.id1=h1.id join highschooler h2 on f.id2=h2.id where h1.grade<>h2.grade;
+------+-----------+-------+------+-----------+-------+
| id1  | name      | grade | id2  | name      | grade |
+------+-----------+-------+------+-----------+-------+
| 1782 | Andrew    |    10 | 1689 | Gabriel   |     9 |
| 1247 | Alexis    |    11 | 1381 | Tiffany   |     9 |
| 1247 | Alexis    |    11 | 1709 | Cassandra |     9 |
| 1689 | Gabriel   |     9 | 1782 | Andrew    |    10 |
| 1316 | Austin    |    11 | 1782 | Andrew    |    10 |
| 1304 | Jordan    |    12 | 1782 | Andrew    |    10 |
| 1381 | Tiffany   |     9 | 1247 | Alexis    |    11 |
| 1709 | Cassandra |     9 | 1247 | Alexis    |    11 |
| 1782 | Andrew    |    10 | 1316 | Austin    |    11 |
| 1934 | Kyle      |    12 | 1316 | Austin    |    11 |
| 1934 | Kyle      |    12 | 1501 | Jessica   |    11 |
| 1782 | Andrew    |    10 | 1304 | Jordan    |    12 |
| 1501 | Jessica   |    11 | 1934 | Kyle      |    12 |
| 1316 | Austin    |    11 | 1934 | Kyle      |    12 |
+------+-----------+-------+------+-----------+-------+
14 rows in set (0.00 sec)

12. What is the average number of friends per student? (Your result should be just one number.) (1 point possible)

mysql> select sum(s1.count)/count(s1.id2) from (select id2, count(*) as count from friend  group by id2)as s1;
+-----------------------------+
| sum(s1.count)/count(s1.id2) |
+-----------------------------+
|                      2.5000 |
+-----------------------------+
1 row in set (0.00 sec)

14. Find the name and grade of the student(s) with the greatest number of friends. (1 point possible)

mysql> select name, grade from (select id1 as id, count(*) as c from friend group by id1)as s1 join Highschooler using (id)where c = (select max(c) from (select id1, count(*) as c from friend group by id1)as s2);
+--------+-------+
| name   | grade |
+--------+-------+
| Andrew |    10 |
| Alexis |    11 |
+--------+-------+
2 rows in set (0.00 sec)X
