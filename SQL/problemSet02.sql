1> CREATE TABLE Location (locationid INT PRIMARY KEY, name VARCHAR(30), sunlight FLOAT, water FLOAT);
2>
3> go
1> INSERT INTO location VALUES(0, "East", .28, .80);
2>
3> INSERT INTO location VALUES(1, "North", .17, .84);
4>
5> INSERT INTO location VALUES(2, "West", .38, .48);
6>
7> INSERT INTO location VALUES(3, "South", .45, .66);
8> go

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)
1> select * from location
2> go
locationid  name                           sunlight                 water
----------- ------------------------------ ------------------------ ------------------------
          0 East                                0.28000000000000003      0.80000000000000004
          1 North                               0.17000000000000001      0.83999999999999997
          2 West                                               0.38      0.47999999999999998
          3 South                               0.45000000000000001      0.66000000000000003

(4 rows affected)

1> CREATE TABLE Plant (plantid INT PRIMARY KEY, name VARCHAR(30), sunlight FLOAT, water FLOAT, weight FLOAT);
2> go
1> INSERT INTO plant VALUES(0, "Carrot", .26, .82, .08);
2>
3> INSERT INTO plant VALUES(1, "Beet", .44, .80, .04);
4>
5> INSERT INTO plant VALUES(2, "Corn", .44, .76, .26);
6>
7> INSERT INTO plant VALUES(3, "Tomato", .42, .80, .16);
8>
9> INSERT INTO plant VALUES(4, "Radish", .28, .84, .02);
10>
11> INSERT INTO plant VALUES(5, "Lettuce", .29, .85, .03);
12>
13> go

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

1> CREATE TABLE planted (plantFK INT, gardenerFK INT, locationFK INT, date1 DATE, seeds INT, FOREIGN KEY(plantFK) REFERENCES plant(plantid), FOREIGN KEY(gardenerFK) REFERENCES gardener(gardenerid), FOREIGN KEY(locationFK) REFERENCES location(locationid));
2> go
1> INSERT INTO planted VALUES(0, 0, 0 , "20120418", 28);
2>
3> INSERT INTO planted VALUES(1, 0, 2, "20120418", 36);
4>
5> INSERT INTO planted VALUES(2, 1, 3, "20120414", 20);
6>
7> INSERT INTO planted VALUES(3, 3, 3, "20120425", 38);
8>
9> INSERT INTO planted VALUES(4, 2, 0, "20120430", 30);
10>
11> go

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

1> CREATE TABLE picked (plantFK INT, gardenerFK INT, locationFK INT, date1 DATE, amount INT, weight FLOAT, FOREIGN KEY(plantFK) REFERENCES plant(plantid), FOREIGN KEY(gardenerFK) REFERENCES gardener(gardenerid), FOREIGN KEY(locationFK) REFERENCES location(locationid));
2> go

1> INSERT INTO picked VALUES(0, 2, 0 ,"20120818", 28, 2.32);
2>
3> INSERT INTO picked VALUES(0, 3, 1 ,"20120816", 12, 1.02);
4>
5> INSERT INTO picked VALUES(2, 1, 3 ,"20120822", 52, 12.96);
6>
7> INSERT INTO picked VALUES(2, 2, 2 ,"20120828", 18, 4.58);
8>
9> INSERT INTO picked VALUES(3, 3, 3 ,"20120822", 15, 3.84);
10>
11> INSERT INTO picked VALUES(4, 2, 0 ,"20120716", 23, 0.52);
12>
13> go

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)