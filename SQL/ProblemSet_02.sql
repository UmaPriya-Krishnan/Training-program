1. Write a valid SQL statement that calculates the total weight of all corn cobs that were picked from the garden:

1> select sum(pic.weight) as weight_of_corn from plant AS Pla join picked as Pic on pla.plantid = pic.plantFK where pla.plantid = pic.plantFK and pla.name='Corn';
2> go
weight_of_corn
------------------------
      17.539999999999999

(1 rows affected)

********************************************************************************************************************************************************
2. For some reason Erin has change his location for picking the tomato to North.
Write the corresponding query.

1> update picked set locationFK =(select locationid from location where name='North') where gardenerFK =( select gardenerid from gardener where name='Erin') and plantFK =(select plantid from plant where name='Tomato') ;
2> go

(1 rows affected)
1> select * from picked ;
2> go
plantFK     gardenerFK  locationFK  date1            amount      weight
----------- ----------- ----------- ---------------- ----------- ------------------------
          0           2           0       2012-08-18          28       2.3199999999999998
          0           3           1       2012-08-16          12                     1.02
          2           1           3       2012-08-22          52       12.960000000000001
          2           2           2       2012-08-28          18       4.5800000000000001
          3           3           1       2012-08-22          15       3.8399999999999999
          4           2           0       2012-07-16          23      0.52000000000000002

(6 rows affected)

*********************************************************************************************************************************************************

3. Insert a new column 'Exper' of type Number (30) to the 'gardener' table which stores Experience of the of person. How will you modify this to varchar2(30).

1> alter table gardener add Exper int;
2> go
1> select * from gardener
2> go
gardenerid  name                           age         Exper
----------- ------------------------------ ----------- -----------
          0 Mother                                  36        NULL
          1 Father                                  38        NULL
          2 Tim                                     15        NULL
          3 Erin                                    12        NULL

(4 rows affected)
1> alter table gardener alter column Exper varchar(30);
2> go
1> select * from gardener
2> go
gardenerid  name                           age         Exper
----------- ------------------------------ ----------- ------------------------------
          0 Mother                                  36 NULL
          1 Father                                  38 NULL
          2 Tim                                     15 NULL
          3 Erin                                    12 NULL

(4 rows affected)

**************************************************************************************************************************

4. Write a query to find the plant name which required seed less
than 20 which plant on 14-apr.

--LESS THAN 20


1> select name from plant where plantid= ( select plantFK from planted where date1='20120414' and seeds<20);
2> go
name
------------------------------

(0 rows affected)

--LESS THAN OR EQUAL TO 

1> select name from plant where plantid= ( select plantFK from planted where date1='20120414' and seeds<=20);
2> go
name
------------------------------
Corn

(1 rows affected)

****************************************************************************************************************************************************************
5. List the amount of sunlight and water to all plants with names that start with letter 'c' or letter 'r'.

1>  select name , sunlight , water from plant where name like 'C%' or name like 'R%';
2> GO
name                           sunlight                 water
------------------------------ ------------------------ ------------------------
Carrot                              0.26000000000000001      0.81999999999999995
Corn                                               0.44      0.76000000000000001
Radish                              0.28000000000000003      0.83999999999999997

(3 rows affected)

******************************************************************************************************************************************************************

6. Write a valid SQL statement that displays the plant name and the total amount of seed required for each plant that were plant in the garden. The output should be in descending order of plant name.

1> select name , sum(seeds) AS total_seeds from plant join planted on plant.plantid=planted.plantFK group by name order by name desc;
2> go
name                           total_seeds
------------------------------ -----------
Tomato                                  76
Radish                                  60
Lettuce                                 30
Corn                                    20
Carrot                                  28
Beet                                    36

(6 rows affected)

*******************************************************************************************************************************************************************
8. Write a valid SQL statement that would produce a result set like the following:8. 

 name |  name  |    date    | amount 
------|--------|------------|-------- 
 Tim  | Radish | 2012-07-16 |     23 
 Tim  | Carrot | 2012-08-18 |     28 
 
 
1> select gardener.name, plant.name , picked.date1, picked.amount from gardener join picked on gardener.gardenerid=picked.gardenerFK join plant on plant.plantid=picked.plantFK where gardener.name='Tim' and picked.locationFK=0;
2> go
name                           name                           date1            amount
------------------------------ ------------------------------ ---------------- -----------
Tim                            Carrot                               2012-08-18          28
Tim                            Radish                               2012-07-16          23

(2 rows affected)

**************************************************************************************************************************************************************************

9. Find out persons who picked from the same location as he/she planted.

1> select name from gardener where gardenerid in (select gardenerFK from planted where gardenerFK in (select gardenerFK from picked));
2> go
name
------------------------------
Father
Tim
Erin

(3 rows affected)

***************************************************************************************************************************************************************************

10. Create a view that lists all the plant names picked from all locations except 'West' in the month of August.

1>  create view Non_WestPlants as select plant.name from plant join picked on plant.plantid=picked.plantFK join location on location.locationid=picked.locationFK where location.name not in ('West') and month(picked.date1)=08 ;
2> go

1> select * from Non_WestPlants
2> go
name
------------------------------
Carrot
Carrot
Corn
Tomato

(4 rows affected)

****************************************************************************************************************************************************************************
