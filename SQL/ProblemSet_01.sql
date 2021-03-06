1. CREATE TABLE hotel(Hotel_no varchar(20) PRIMARY KEY, Name varchar(20), City varchar(20));
2. CREATE TABLE Room(Room_no INT PRIMARY KEY, Hotel_no varchar(20), Type varchar(10), Price float(10), FOREIGN key(Hotel_no) REFERENCES Hotel(Hotel_no));
3. CREATE TABLE Guest (Guest_no varchar(10), Name varchar(20), City varchar(20));
4.CREATE TABLE Booking(Hotel_No varchar(20),Guest_No varchar(10),Date_From VARCHAR(20),Date_To VARCHAR(20), Room_No INT,FOREIGN KEY(Hotel_No) REFERENCES Hotel(Hotel_No),FOREIGN KEY(Guest_No) REFERENCES Guest(Guest_No),FOREIGN KEY(Room_No) REFERENCES Room(Room_No));


1> INSERT INTO Hotel(Hotel_no, Name, City) VALUES('H111', 'Empire Hotel', 'New York');
2> go

(1 rows affected)
1> INSERT INTO Hotel(Hotel_no, Name, City) VALUES('H235', 'Park Place', 'New York');
2> go

(1 rows affected)
1> INSERT INTO Hotel(Hotel_no, Name, City) VALUES('H432', 'Brownstone Hotel', 'Toronto');
2> go

(1 rows affected)
1> INSERT INTO Hotel(Hotel_no, Name, City) VALUES('H498', 'James Plaza', 'Toronto');
2> go

(1 rows affected)
1> INSERT INTO Hotel(Hotel_no, Name, City) VALUES('H193', 'Devon Hotel', 'Boston');
2> go

(1 rows affected)
1> INSERT INTO Hotel(Hotel_no, Name, City) VALUES('H437', 'Clairmont Hotel', 'Boston');
2> go

(1 rows affected)

(2 rows affected)
1> INSERT INTO Room(Room_No,Hotel_No,Type,Price) VALUES(1267,'H235','N',175.00);
2> go

(1 rows affected)
1> INSERT INTO Room(Room_No,Hotel_No,Type,Price) VALUES(1289,'H235','N',195.00);
2>
3> go

(1 rows affected)
1> INSERT INTO Room(Room_No,Hotel_No,Type,Price) VALUES(876,'H432','S',124.00);
2> go

(1 rows affected)
1> INSERT INTO Room(Room_No,Hotel_No,Type,Price) VALUES(898,'H432','S',124.00);
2>
3> go

(1 rows affected)
1> INSERT INTO Room(Room_No,Hotel_No,Type,Price) VALUES(345,'H498','N',160.00);
2>  go

(1 rows affected)
1> INSERT INTO Room(Room_No,Hotel_No,Type,Price) VALUES(467,'H498','N',180.00);
2>
3> go

(1 rows affected)
1> INSERT INTO Room(Room_No,Hotel_No,Type,Price) VALUES(1001,'H193','S',150.00);
2> go

(1 rows affected)
1> INSERT INTO Room(Room_No,Hotel_No,Type,Price) VALUES(1201,'H193','N',175.00);
2> go

(1 rows affected)
1> INSERT INTO Room(Room_No,Hotel_No,Type,Price) VALUES(257,'H437','N',140.00);
2> go

(1 rows affected)
1>  INSERT INTO Room(Room_No,Hotel_No,Type,Price) VALUES(223,'H437','N',155.00);
2> go

(1 rows affected)
1>INSERT INTO Guest(Guest_No,Name,City) VALUES ('G256','Adam Wayne','Pittsburgh');
2>
3>INSERT INTO Guest(Guest_No,Name,City) VALUES ('G367','Tara Cummings','Baltimore');
4>
5>INSERT INTO Guest(Guest_No,Name,City) VALUES ('G879','Vanessa Parry','Pittsburgh');
6>
7>INSERT INTO Guest(Guest_No,Name,City) VALUES ('G230','Tom Hancock','Philadelphia');
8>
9>INSERT INTO Guest(Guest_No,Name,City) VALUES ('G467','Robert Swift','Atlanta');
10>go

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)

(1 rows affected)


1>  INSERT INTO Guest(Guest_No,Name,City) VALUES ('G190','Edward Cane','Baltimore');
2> go

(1 rows affected)
1> INSERT INTO Booking(Hotel_No,Guest_No,Date_From,Date_To,Room_No) VALUES('H111','G256','10-Aug-99','15-AUG-99',412);
2> INSERT INTO Booking(Hotel_No,Guest_No,Date_From,Date_To,Room_No) VALUES('H111','G367','18-AUG-99','21-AUG-99',412);
3> INSERT INTO Booking(Hotel_No,Guest_No,Date_From,Date_To,Room_No) VALUES('H235','G879','05-SEP-99','12-SEP-99',1267);
4> INSERT INTO Booking(Hotel_No,Guest_No,Date_From,Date_To,Room_No) VALUES('H498','G230','15-SEP-99','18-SEP-99',467);
5> INSERT INTO Booking(Hotel_No,Guest_No,Date_From,Date_To,Room_No) VALUES('H498','G256','30-NOV-99','02-DEC-99',345);
6> INSERT INTO Booking(Hotel_No,Guest_No,Date_From,Date_To,Room_No) VALUES('H498','G467','03-NOV-99','05-NOV-99',345);
7> INSERT INTO Booking(Hotel_No,Guest_No,Date_From,Date_To,Room_No) VALUES('H193','G190','15-NOV-99','19-NOV-99',1001);
8> INSERT INTO Booking(Hotel_No,Guest_No,Date_From,Date_To,Room_No) VALUES('H193','G367','12-SEP-99','14-SEP-99',1001);
9> INSERT INTO Booking(Hotel_No,Guest_No,Date_From,Date_To,Room_No) VALUES('H193','G367','01-OCT-99','06-OCT-99',1201);
10> INSERT INTO Booking(Hotel_No,Guest_No,Date_From,Date_To,Room_No) VALUES('H437','G190','04-OCT-99 ','06-OCT-99 ',223);
11> INSERT INTO Booking(Hotel_No,Guest_No,Date_From,Date_To,Room_No) VALUES('H437','G879','14-SEP-99','17-SEP-99',223);
12> GO

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
******************************************************************************************************
******************************************************************************************************

1. List full details of all hotels.

1> SELECT * FROM Hotel
2> SELECT * FROM Room
3> SELECT * FROM Booking
4> SELECT * FROM Guest
5> go

Hotel_no             Name                 City
-------------------- -------------------- --------------------
H111                 Empire Hotel         New York
H193                 Devon Hotel          Boston
H235                 Park Place           New York
H432                 Brownstone Hotel     Toronto
H437                 Clairmont Hotel      Boston
H498                 James Plaza          Toronto

(6 rows affected)
Room_no     Hotel_no             Type       Price
----------- -------------------- ---------- --------------
        223 H437                 N                   155.0
        257 H437                 N                   140.0
        313 H111                 S                   145.0
        345 H498                 N                   160.0
        412 H111                 N                   145.0
        467 H498                 N                   180.0
        876 H432                 S                   124.0
        898 H432                 S                   124.0
       1001 H193                 S                   150.0
       1201 H193                 N                   175.0
       1267 H235                 N                   175.0
       1289 H235                 N                   195.0

(12 rows affected)
Hotel_No             Guest_No   Date_From            Date_To              Room_No
-------------------- ---------- -------------------- -------------------- -----------
H111                 G256       10-Aug-99            15-AUG-99                    412
H111                 G367       18-AUG-99            21-AUG-99                    412
H235                 G879       05-SEP-99            12-SEP-99                   1267
H498                 G230       15-SEP-99            18-SEP-99                    467
H498                 G256       30-NOV-99            02-DEC-99                    345
H498                 G467       03-NOV-99            05-NOV-99                    345
H193                 G190       15-NOV-99            19-NOV-99                   1001
H193                 G367       12-SEP-99            14-SEP-99                   1001
H193                 G367       01-OCT-99            06-OCT-99                   1201
H437                 G190       04-OCT-99            06-OCT-99                    223
H437                 G879       14-SEP-99            17-SEP-99                    223

(11 rows affected)
Guest_no   Name                 City
---------- -------------------- --------------------
G190       Edward Cane          Baltimore
G230       Tom Hancock          Philadelphia
G256       Adam Wayne           Pittsburgh
G367       Tara Cummings        Baltimore
G467       Robert Swift         Atlanta
G879       Vanessa Parry        Pittsburgh

(6 rows affected)

*******************************************************************************************************
2. List full details of all hotels in New York.

1> select * from hotel where city = 'New York'
2> go
Hotel_no             Name                 City
-------------------- -------------------- --------------------
H111                 Empire Hotel         New York
H235                 Park Place           New York

********************************************************************************************************
3. List the names and cities of all guests, ordered according to their cities.

1>select name,city from guest order by city
2> go
name                 city
-------------------- --------------------
Robert Swift         Atlanta
Edward Cane          Baltimore
Tara Cummings        Baltimore
Tom Hancock          Philadelphia
Adam Wayne           Pittsburgh
Vanessa Parry        Pittsburgh

(6 rows affected)

*******************************************************************************************************
4. List all details for non-smoking rooms in ascending order of price.

1> SELECT * FROM Room where Type = 'N' ORDER BY Price
2> go
Room_no     Hotel_no             Type       Price
----------- -------------------- ---------- --------------
        257 H437                 N                   140.0
        412 H111                 N                   145.0
        223 H437                 N                   155.0
        345 H498                 N                   160.0
       1201 H193                 N                   175.0
       1267 H235                 N                   175.0
        467 H498                 N                   180.0
       1289 H235                 N                   195.0

(8 rows affected)

*********************************************************************************************************
5. List the number of hotels there are.

1> SELECT COUNT(Hotel_no) AS Count from Hotel
2> go
Count
-----------
          6
		  
*********************************************************************************************************		  
6. List the cities in which guests live. Each city should be listed only once.

1> SELECT DISTINCT City FROM Guest
2> go
City
--------------------
Atlanta
Baltimore
Philadelphia
Pittsburgh

(4 rows affected)

********************************************************************************************************
7. List the average price of a room.

1> SELECT AVG(Price) from Room
2> go

------------------------
      155.66666666666666
	  
*********************************************************************************************************	  
8. List hotel names, their room numbers, and the type of that room.

1> SELECT Name, Room_no, Type from Hotel as H INNER JOIN Room as R ON H.Hotel_no = R.Hotel_No
2> go
Name                 Room_no     Type
-------------------- ----------- ----------
Clairmont Hotel              223 N
Clairmont Hotel              257 N
Empire Hotel                 313 S
James Plaza                  345 N
Empire Hotel                 412 N
James Plaza                  467 N
Brownstone Hotel             876 S
Brownstone Hotel             898 S
Devon Hotel                 1001 S
Devon Hotel                 1201 N
Park Place                  1267 N
Park Place                  1289 N

****************************************************************************************************************

9. List the hotel names, booking dates, and room numbers for all hotels in New York.

1> SELECT Name, Room_no, Date_From, Date_to FROM Hotel as H INNER JOIN Booking as B ON H.Hotel_no = B.Hotel_no where H.city = 'New York'
2> go
Name                 Room_no     Date_From            Date_to
-------------------- ----------- -------------------- --------------------
Empire Hotel                 412 10-Aug-99            15-AUG-99
Empire Hotel                 412 18-AUG-99            21-AUG-99
Park Place                  1267 05-SEP-99            12-SEP-99

(3 rows affected)

********************************************************************************************************************
10. What is the number of bookings that started in the month of September?

1> Select count(*) as count from booking where Date_from like '%SEP%';
2> go
count
-----------
          4

(1 rows affected)

***********************************************************************************************************************
11. List the names and cities of guests who began a stay in New York in August.

select guest.Name , guest.City from guest join booking on guest.Guest_No=booking.Guest_No where month(booking.Date_From)>=08 and booking.Hotel_No in ( select hotel.Hotel_No from hotel where hotel.City='New York');

Name                 City
-------------------- --------------------
Adam Wayne           Pittsburgh
Tara Cummings        Baltimore
Vanessa Parry        Pittsburgh

(3 rows affected)

**********************************************************************************************************************
12. List the hotel names and room numbers of any hotel rooms that have not been booked.

1> select name,Room_no from hotel as H join room as R on H.hotel_no = R.hotel_no where R.room_no not in (select booking.room_no from booking);
2> go
name                 Room_no
-------------------- -----------
Clairmont Hotel              257
Empire Hotel                 313
Brownstone Hotel             876
Brownstone Hotel             898
Park Place                  1289

(5 rows affected)

**************************************************************************************************************************
13. List the hotel name and city of the hotel with the highest priced room.

1> SELECT name, city from hotel as H join Room as R on H.hotel_no = R.hotel_no where price = (select max(price) from room);
2> go
name                 city
-------------------- --------------------
Park Place           New York

(1 rows affected)

***************************************************************************************************************************

14. List hotel names, room numbers, cities, and prices for hotels that have rooms with prices lower than the lowest priced room in a Boston hotel.
1>  select hotel.Name , hotel.City , room.Room_No,room.Price from hotel join room on hotel.Hotel_No=room.Hotel_No where room.Price < (select min(room.Price) from room join hotel on room.Hotel_No=hotel.Hotel_No where hotel.City='Boston');
2>
3> go
Name                 City                 Room_No     Price
-------------------- -------------------- ----------- --------------
Brownstone Hotel     Toronto                      876          124.0
Brownstone Hotel     Toronto                      898          124.0

(2 rows affected) 

******************************************************************************************************************************
15. List the average price of a room grouped by city.

1> select city,avg(price) as average from hotel as H join room as R on H.hotel_no = R.hotel_no group by H.city;
2> go
city                 average
-------------------- ------------------------
Boston                                  155.0
New York                                165.0
Toronto                                 147.0

(3 rows affected)
