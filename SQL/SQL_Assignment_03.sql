create table stats(Stats_ID	 int, MONTH int, 	YEAr int, TEMP_FARENHEIT float, 	RAIN_INCH float);;

insert into stats values (13, 1, 2010, 57.4, 0.31);
insert into stats values (13, 5, 2010, 91.7, 5.15);
insert into stats values (13, 12, 2010, 12.6, 8.34);
insert into stats values (13, 9, 2010, 100.3, 10.34);
insert into stats values (44, 9, 2010, 27.2, 3.45);
insert into stats values (44, 2, 2010, 27.3, 0.18);
insert into stats values (44, 6, 2010, 74.8, 2.11);
insert into stats values (66, 3, 2010, 6.7, 2.1);
insert into stats values (66, 7, 2010, 65.8, 4.52);

create table station (Station_ID int, CITY varchar(20), STATE varchar(10), LAT_N int, LONG_W int);

insert into station values (13, 'Phoenix', 'AZ',33,112);
insert into station values (44,'Denver', 'CO', 40, 105);
insert into station values (66,'Caribou','ME',47,68);



1. mysql> select * from(select st.city,temp_farenheit,rain_inch,dense_rank()
    -> over(partition by stats_id order by temp_farenheit desc,rain_inch desc)as a from
    -> stats s join station st on s.stats_id=st.station_id)as s where a=1;
+---------+----------------+-----------+---+
| city    | temp_farenheit | rain_inch | a |
+---------+----------------+-----------+---+
| Phoenix |          100.3 |     10.34 | 1 |
| Denver  |           74.8 |      2.11 | 1 |
| Caribou |           65.8 |      4.52 | 1 |
+---------+----------------+-----------+---+
3 rows in set (0.02 sec)


2. mysql> select st.station_id,st.city,st.state,s.month,s.year,round((temp_farenheit-32)*(5/9),2) as celcius,
    ->   round((s.rain_inch*03937),2) as cm from station st join stats s on st.station_id=s.stats_id;
+------------+---------+-------+-------+------+---------+----------+
| station_id | city    | state | month | year | celcius | cm       |
+------------+---------+-------+-------+------+---------+----------+
|         13 | Phoenix | AZ    |     1 | 2010 |   14.11 |  1220.47 |
|         13 | Phoenix | AZ    |     5 | 2010 |   33.17 | 20275.55 |
|         13 | Phoenix | AZ    |    12 | 2010 |  -10.78 | 32834.58 |
|         13 | Phoenix | AZ    |     9 | 2010 |   37.94 | 40708.58 |
|         44 | Denver  | CO    |     9 | 2010 |   -2.67 | 13582.65 |
|         44 | Denver  | CO    |     2 | 2010 |   -2.61 |   708.66 |
|         44 | Denver  | CO    |     6 | 2010 |   23.78 |  8307.07 |
|         66 | Caribou | ME    |     3 | 2010 |  -14.06 |  8267.70 |
|         66 | Caribou | ME    |     7 | 2010 |   18.78 | 17795.24 |
+------------+---------+-------+-------+------+---------+----------+
9 rows in set (0.12 sec)

3. Display all rows for states on all quarters. If a state do not have any quarter information,
 default Temp in Celcius and rain in cms based on average for the year

mysql>  select stats_id,month,year,temp_farenheit,rain_inch,
    -> station_id,city,state,lat_n,long_w from station t left join stats s on s.stats_id=t.station_id group by month having
    -> month in (select month from (SELECT month,case when month>=1 and month<=3 then 'q1'
    -> when month>=4 and month<=6 then 'q2' when month>=7 and month<=9 then 'q3'
    -> when month>=10 and month<=12 then 'q4' else 'q' end as q
    ->  from stats group by q) d);
+----------+-------+------+----------------+-----------+------------+---------+-------+-------+--------+
| stats_id | month | year | temp_farenheit | rain_inch | station_id | city    | state | lat_n | long_w |
+----------+-------+------+----------------+-----------+------------+---------+-------+-------+--------+
|       13 |     1 | 2010 |           57.4 |      0.31 |         13 | Phoenix | AZ    |    33 |    112 |
|       13 |     5 | 2010 |           91.7 |      5.15 |         13 | Phoenix | AZ    |    33 |    112 |
|       13 |    12 | 2010 |           12.6 |      8.34 |         13 | Phoenix | AZ    |    33 |    112 |
|       13 |     9 | 2010 |          100.3 |     10.34 |         13 | Phoenix | AZ    |    33 |    112 |
+----------+-------+------+----------------+-----------+------------+---------+-------+-------+--------+
4 rows in set (1.61 sec)


4. Which state has coldest month and highest rainfall compared to average per year

  mysql> select city,state,rain_inch,avg_rain,avg_temp from (select city,state,temp_farenheit,rain_inch,avg_rain,avg_temp,
    ->   dense_rank() over(partition by state order by avg_rain desc,avg_temp desc) rank_avg from (select city,state,
    ->   temp_farenheit,rain_inch,avg(rain_inch) over() as avg_rain,avg(temp_farenheit) over() as avg_temp from stats s 
    ->   join station s1 on s.stats_id=s1.station_id) as rain_temp where avg_rain<rain_inch and avg_temp > temp_farenheit) as
    ->   max_rain where rank_avg=1;
+---------+-------+-----------+-------------------+------------------+
| city    | state | rain_inch | avg_rain          | avg_temp         |
+---------+-------+-----------+-------------------+------------------+
| Phoenix | AZ    |      8.34 | 4.055555582046509 | 51.5333342022366 |
+---------+-------+-----------+-------------------+------------------+
1 row in set (0.13 sec)

5. Which city had maximum rainfall below average . Display city, state, rainfall, average information

mysql> select city,state,rain_inch,avg from (select city,state,rain_inch,dense_rank()over(order by rain_inch desc) as rank1,
    -> avg from(select s1.city,s1.state,temp_farenheit,rain_inch,avg(rain_inch) over() as avg from stats s join station s1 on
    -> s.stats_id=s1.station_id)a where rain_inch<avg)a where rank1=1 ;
+--------+-------+-----------+-------------------+
| city   | state | rain_inch | avg               |
+--------+-------+-----------+-------------------+
| Denver | CO    |      3.45 | 4.055555582046509 |
+--------+-------+-----------+-------------------+
1 row in set (0.00 sec)


6. Which city had second  coldest month when compared to national average

mysql> select * from
    -> (select st.stats_id,s.city,st.month,st.TEMP_FARENHEIT,st.rain_inch,dense_rank() over(partition by st.stats_id
    -> order by st.TEMP_FARENHEIT asc,st.rain_inch desc ) as ra
    -> from stats st join station s on
    -> s.station_id=st.stats_id )d
    -> where ra=1 and rain_inch > (select avg(rain_inch) from stats) ;
+----------+---------+-------+----------------+-----------+----+
| stats_id | city    | month | TEMP_FARENHEIT | rain_inch | ra |
+----------+---------+-------+----------------+-----------+----+
|       13 | Phoenix |    12 |           12.6 |      8.34 |  1 |
+----------+---------+-------+----------------+-----------+----+
1 row in set (0.00 sec)


7. create a view based on question#3. 
If you query view, you should have resultset matching with question #3

mysql> create view third as select stats_id,month,year,temp_farenheit,rain_inch,
    -> station_id,city,state,lat_n,long_w from station t left join stats s on s.stats_id=t.station_id group by month having
    -> month in (select month from (SELECT month,case when month>=1 and month<=3 then 'q1'
    -> when month>=4 and month<=6 then 'q2' when month>=7 and month<=9 then 'q3'
    -> when month>=10 and month<=12 then 'q4' else 'q' end as q
    ->  from stats group by q) as b);
Query OK, 0 rows affected (0.88 sec)

mysql> select * from third ;
+----------+-------+------+----------------+-----------+------------+---------+-------+-------+--------+
| stats_id | month | year | temp_farenheit | rain_inch | station_id | city    | state | lat_n | long_w |
+----------+-------+------+----------------+-----------+------------+---------+-------+-------+--------+
|       13 |     1 | 2010 |           57.4 |      0.31 |         13 | Phoenix | AZ    |    33 |    112 |
|       13 |     5 | 2010 |           91.7 |      5.15 |         13 | Phoenix | AZ    |    33 |    112 |
|       13 |    12 | 2010 |           12.6 |      8.34 |         13 | Phoenix | AZ    |    33 |    112 |
|       13 |     9 | 2010 |          100.3 |     10.34 |         13 | Phoenix | AZ    |    33 |    112 |
+----------+-------+------+----------------+-----------+------------+---------+-------+-------+--------+
4 rows in set (0.01 sec)


9. Report stations which obsevered temperatures less than 0(in celcius)

mysql> select station_id, celcius from (select st.station_id,round((temp_farenheit-32)*(5/9),2) as celcius from station st join stats s on st.station_id=s.stats_id)a
    ->   where celcius<0;
+------------+---------+
| station_id | celcius |
+------------+---------+
|         13 |  -10.78 |
|         44 |   -2.67 |
|         44 |   -2.61 |
|         66 |  -14.06 |
+------------+---------+
4 rows in set (0.00 sec)


10. Display state information and number of times when rainfall is greater than national avergae

mysql> select city, state,count(city) from (select s1.city,s1.state,s.month,s.rain_inch,avg(s.rain_inch) over() as avg
    from stats s join station s1 on s.stats_id=s1.station_id) derv_tab where rain_inch>avg group by city;
+---------+-------+-------------+
| city    | state | count(city) |
+---------+-------+-------------+
| Phoenix | AZ    |           3 |
| Caribou | ME    |           1 |
+---------+-------+-------------+
2 rows in set (0.77 sec)

