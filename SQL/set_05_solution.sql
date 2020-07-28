1) Give the organisers name of the concert in the Assembly Rooms after the first of Feb, 1997. (1 point possible)
mysql> select m.m_name from musician m join concert c on c.concert_orgniser=m.m_no
    -> where concert_venue="Assembly Rooms" and con_date>01/02/1997;
+---------------+
| m_name        |
+---------------+
| James Steeple |
+---------------+
1 row in set (0.00 sec)


2) Find all the performers who played guitar or violin and were born in England. (1 point possible)

mysql> select m.m_name from performer p join musician m on m.m_no  = p.perf_is
    -> join place pl on pl.place_no = m.born_in
    -> where (p.instrument = 'violin' OR p.instrument = 'guitar') and (pl.place_country = 'England');
+------------------+
| m_name           |
+------------------+
| Harry Forte      |
| Davis Heavan     |
| Alan Fluff       |
| Theo Mengel      |
| James First      |
| Harriet Smithson |
+------------------+
6 rows in set (0.02 sec)

3) List the names of musicians who have conducted concerts in USA together with the towns and dates of these concerts. 

mysql> select m.m_name,p.place_town,c.con_date from concert c join place p on c.concert_in=p.place_no join 
musician m on m.m_no=c.concert_orgniser where p.place_country="usa";
+---------------+------------+---------------------+
| m_name        | place_town | con_date            |
+---------------+------------+---------------------+
| James Steeple | New York   | 1997-06-15 00:00:00 |
+---------------+------------+---------------------+
1 row in set (0.00 sec)

4) How many concerts have featured at least one composition by Andy Jones? List concert date, venue and the composition title

mysql> select m_name,con_date,concert_venue,c_title from musician m join composer c on m_no=comp_is join has_composed on comp_no=cmpr_no join composition on cmpn_no=c_no join performance on c_no=performed join concert on performed_in=concert_no where m_name='andy jones';
+------------+---------------------+---------------+----------------+
| m_name     | con_date            | concert_venue | c_title        |
+------------+---------------------+---------------+----------------+
| Andy Jones | 1997-06-15 00:00:00 | Metropolitan  | A Simple Piece |
+------------+---------------------+---------------+----------------+
1 row in set (0.02 sec)

5) List the different instruments played by the musicians and avg number of musicians who play the instrument

mysql> select instrument,avg(ins) from (select instrument,perf_is,count(instrument) as ins from performer group by perf_is) emp group by instrument;
+------------+----------+
| instrument | avg(ins) |
+------------+----------+
| violin     |   2.2000 |
| viola      |   2.5000 |
| banjo      |   3.0000 |
| guitar     |   3.0000 |
| trumpet    |   2.0000 |
| bass       |   3.0000 |
| horn       |   1.0000 |
| cello      |   1.0000 |
+------------+----------+
8 rows in set (0.01 sec)


6) List the names, dates of birth and the instrument played of living musicians who play a instrument which Theo also plays

mysql> select   m1.m_name,m1.born,p1.instrument from musician m1 join performer p1 on p1.perf_is = m1.m_no
    -> where m1.died is null and instrument in
    -> (select  p.instrument from performer p join musician  m
    -> on p.perf_is = m.m_no where m.m_name LIKE '%Theo%');
+-------------+---------------------+------------+
| m_name      | born                | instrument |
+-------------+---------------------+------------+
| John Smith  | 1950-03-03 00:00:00 | violin     |
| Theo Mengel | 1948-08-12 00:00:00 | banjo      |
| Harry Forte | 1951-02-28 00:00:00 | violin     |
| Theo Mengel | 1948-08-12 00:00:00 | violin     |
| Harry Forte | 1951-02-28 00:00:00 | drums      |
| Jeff Dawn   | 1945-12-12 00:00:00 | violin     |
| James First | 1965-06-10 00:00:00 | violin     |
| Theo Mengel | 1948-08-12 00:00:00 | drums      |
+-------------+---------------------+------------+
8 rows in set (0.11 sec)

7) List the name and the number of players for the band whose number of players is greater than the average number of players in each band

mysql> select band_name,count(player) from plays_in join band on band_no=band_id group by band_name having count(player)> (select avg(number) from ( select count(player) number from plays_in group by band_id) mus);
+-----------+---------------+
| band_name | count(player) |
+-----------+---------------+
| ROP       |             7 |
| Oh well   |             6 |
| AASO      |             7 |
+-----------+---------------+
3 rows in set (0.00 sec)

8) List the names of musicians who both conduct and compose and live in Britain

mysql> select distinct m.m_name from concert c   join composer cp on cp.comp_is  = c.concert_orgniser
    -> join musician m on m.m_no = cp.comp_is  join place p
    -> on p.place_no = m.living_in where p.place_country = 'England' ;
+-------------+
| m_name      |
+-------------+
| Helen Smyth |
+-------------+
1 row in set (0.00 sec)




