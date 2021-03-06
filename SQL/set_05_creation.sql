mysql> create table plays_in(player    integer not null references performer (perf_no),band_id   integer not null references band (band_no),primary key ( player, band_id));
Query OK, 0 rows affected (0.21 sec)

mysql> create table composition(c_no integer not null primary key,comp_date DATETIME,c_title varchar(40) not null,c_in integer references place (place_no));
Query OK, 0 rows affected (0.11 sec)

mysql> create table has_composed(cmpr_no   integer not null  references composer (comp_no),cmpn_no   integer not null  references composition (c_no),primary key ( cmpr_no, cmpn_no ));
Query OK, 0 rows affected (0.10 sec)

mysql> create table concert(concert_no  integer not null    primary key,concert_venue varchar(20),concert_in  integer not null  references place (place_no),con_date DATETIME,concert_orgniser integer    references musician (m_no) );
Query OK, 0 rows affected (0.14 sec)

mysql> create table performance(pfrmnc_no integer not null primary key,gave    integer references band (band_no),performed integer references composition(c_no),conducted_by  integer references musician (m_no),performed_in  integer references concert (concert_no));
Query OK, 0 rows affected (0.23 sec)


insert into place values (1,'Manchester','England');
insert into place values (2,'Edinburgh','Scotland');
insert into place values (3,'Salzburg','Austria');
insert into place values (4,'New York','USA');
insert into place values (5,'Birmingham','England');
insert into place values (6,'Glasgow','Scotland');
insert into place values (7,'London','England');
insert into place values (8,'Chicago','USA');
insert into place values (9,'Amsterdam','Netherlands');

Query OK, 1 row affected (0.03 sec)

Query OK, 1 row affected (0.01 sec)

Query OK, 1 row affected (0.01 sec)

Query OK, 1 row affected (0.02 sec)

Query OK, 1 row affected (0.01 sec)

Query OK, 1 row affected (0.01 sec)

Query OK, 1 row affected (0.01 sec)

Query OK, 1 row affected (0.01 sec)

Query OK, 1 row affected (0.01 sec)


insert into musician values (1,'Fred Bloggs','1948-01-02',NULL,1,2);
insert into musician values (2,'John Smith','1950-03-03',NULL,3,4);
insert into musician values (3,'Helen Smyth','1948-08-08',NULL,4,5);
insert into musician values (4,'Harriet Smithson','1909-05-09','1980-09-20',5,6);
insert into musician values (5,'James First','1965-06-10',NULL,7,7);
insert into musician values (6,'Theo Mengel','1948-08-12',NULL,7,1);
insert into musician values (7,'Sue Little','1945-02-21',NULL,8,9);
insert into musician values (8,'Harry Forte','1951-02-28',NULL,1,8);
insert into musician values (9,'Phil Hot','1942-06-30',NULL,2,7);
insert into musician values (10,'Jeff Dawn','1945-12-12',NULL,3,6);
insert into musician values (11,'Rose Spring','1948-05-25',NULL,4,5);
insert into musician values (12,'Davis Heavan','1975-10-03',NULL,5,4);
insert into musician values (13,'Lovely Time','1948-12-28',NULL,6,3);
insert into musician values (14,'Alan Fluff','1935-01-15','1997-05-15',7,2);
insert into musician values (15,'Tony Smythe','1932-04-02',NULL,8,1);
insert into musician values (16,'James Quick','1924-08-08',NULL,9,2);
insert into musician values (17,'Freda Miles','1920-07-04',NULL,9,3);
insert into musician values (18,'Elsie James','1947-05-06',NULL,8,5);
insert into musician values (19,'Andy Jones','1958-10-08',NULL,7,6);
insert into musician values (20,'Louise Simpson','1948-01-10','1998-02-11',6,6);
insert into musician values (21,'James Steeple','1947-01-10',NULL,5,6);
insert into musician values (22,'Steven Chaytors','1956-03-11',NULL,6,7);



insert into performer values (1,2,'violin','classical');
insert into performer values (2,4,'viola','classical');
insert into performer values (3,6,'banjo','jazz');
insert into performer values (4,8,'violin','classical');
insert into performer values (5,12,'guitar','jazz');
insert into performer values (6,14,'violin','classical');
insert into performer values (7,16,'trumpet','jazz');
insert into performer values (8,18,'viola','classical');
insert into performer values (9,20,'bass','jazz');
insert into performer values (10,2,'flute','jazz');
insert into performer values (11,20,'cornet','jazz');
insert into performer values (12,6,'violin','jazz');
insert into performer values (13,8,'drums','jazz');
insert into performer values (14,10,'violin','classical');
insert into performer values (15,12,'cello','classical');
insert into performer values (16,14,'viola','classical');
insert into performer values (17,16,'flute','jazz');
insert into performer values (18,18,'guitar','not known');
insert into performer values (19,20,'trombone','jazz');
insert into performer values (20,3,'horn','jazz');
insert into performer values (21,5,'violin','jazz');
insert into performer values (22,7,'cello','classical');
insert into performer values (23,2,'bass','jazz');
insert into performer values (24,4,'violin','jazz');
insert into performer values (25,6,'drums','classical');
insert into performer values (26,8,'clarinet','jazz');
insert into performer values (27,10,'bass','jazz');
insert into performer values (28,12,'viola','classical');
insert into performer values (29,18,'cello','classical');



insert into composer values (1,1,'jazz');
insert into composer values (2,3,'classical');
insert into composer values (3,5,'jazz');
insert into composer values (4,7,'classical');
insert into composer values (5,9,'jazz');
insert into composer values (6,11,'rock');
insert into composer values (7,13,'classical');
insert into composer values (8,15,'jazz');
insert into composer values (9,17,'classical');
insert into composer values (10,19,'jazz');
insert into composer values (11,10,'rock');
insert into composer values (12,8,'jazz');


insert into band values (1,'ROP',5,'classical','1930-01-01',11);
insert into band values (2,'AASO',6,'classical',NULL,10);
insert into band values (3,'The J Bs',8,'jazz',NULL,12);
insert into band values (4,'BBSO',9,'classical',NULL,21);
insert into band values (5,'The left Overs',2,'jazz',NULL,8);
insert into band values (6,'Somebody Loves this',1,'jazz',NULL,6);
insert into band values (7,'Oh well',4,'classical',NULL,3);
insert into band values (8,'Swinging strings',4,'classical',NULL,7);
insert into band values (9,'The Rest',9,'jazz',NULL,16);


insert into plays_in values (1,1);
insert into plays_in values (1,7);
insert into plays_in values (3,1);
insert into plays_in values (4,1);
insert into plays_in values (4,7);
insert into plays_in values (5,1);
insert into plays_in values (6,1);
insert into plays_in values (6,7);
insert into plays_in values (7,1);
insert into plays_in values (8,1);
insert into plays_in values (8,7);
insert into plays_in values (10,2);
insert into plays_in values (12,2);
insert into plays_in values (13,2);
insert into plays_in values (14,2);
insert into plays_in values (14,8);
insert into plays_in values (15,2);
insert into plays_in values (15,8);
insert into plays_in values (17,2);
insert into plays_in values (18,2);
insert into plays_in values (19,3);
insert into plays_in values (20,3);
insert into plays_in values (21,4);
insert into plays_in values (22,4);
insert into plays_in values (23,4);
insert into plays_in values (25,5);
insert into plays_in values (26,6);
insert into plays_in values (27,6);
insert into plays_in values (28,7);
insert into plays_in values (28,8);
insert into plays_in values (29,7);


insert into composition values (1,'1975-06-17','Opus 1',1);
insert into composition values (2,'1976-07-21','Here Goes',2);
insert into composition values (3,'1981-12-14','Valiant Knight',3);
insert into composition values (4,'1982-01-12','Little Piece',4);
insert into composition values (5,'1985-03-13','Simple Song',5);
insert into composition values (6,'1986-04-14','Little Swing Song',6);
insert into composition values (7,'1987-05-13','Fast Journey',7);
insert into composition values (8,'1976-02-14','Simple Love Song',8);
insert into composition values (9,'1982-01-21','Complex Rythms',9);
insert into composition values (10,'1985-02-23','Drumming Rythms',9);
insert into composition values (11,'1978-03-18','Fast Drumming',8);
insert into composition values (12,'1984-08-13','Slow Song',7);
insert into composition values (13,'1968-09-14','Blue Roses',6);
insert into composition values (14,'1983-11-15','Velvet Rain',5);
insert into composition values (15,'1982-05-16','Cold Wind',4);
insert into composition values (16,'1983-06-18','After the Wind Blows',3);
insert into composition values (17,NULL,'A Simple Piece',2);
insert into composition values (18,'1985-01-12','Long Rythms',1);
insert into composition values (19,'1988-02-12','Eastern Wind',1);
insert into composition values (20,NULL,'Slow Symphony Blowing',2);
insert into composition values (21,'1990-07-12','A Last Song',6);


insert into has_composed values (1,1);
insert into has_composed values (1,8);
insert into has_composed values (2,11);
insert into has_composed values (3,2);
insert into has_composed values (3,13);
insert into has_composed values (3,14);
insert into has_composed values (3,18);
insert into has_composed values (4,12);
insert into has_composed values (4,20);
insert into has_composed values (5,3);
insert into has_composed values (5,13);
insert into has_composed values (5,14);
insert into has_composed values (6,15);
insert into has_composed values (6,21);
insert into has_composed values (7,4);
insert into has_composed values (7,9);
insert into has_composed values (8,16);
insert into has_composed values (9,5);
insert into has_composed values (9,10);
insert into has_composed values (10,17);
insert into has_composed values (11,6);
insert into has_composed values (12,7);
insert into has_composed values (12,19);


insert into concert values (1,'Bridgewater Hall',1,'1995-01-06',21);
insert into concert values (2,'Bridgewater Hall',1,'1996-05-08',3);
insert into concert values (3,'Usher Hall',2,'1995-06-03',3);
insert into concert values (4,'Assembly Rooms',2,'1997-09-20',21);
insert into concert values (5,'Festspiel Haus',3,'1995-02-21',8);
insert into concert values (6,'Royal Albert Hall',7,'1993-04-12',8);
insert into concert values (7,'Concertgebouw',9,'1993-05-14',8);
insert into concert values (8,'Metropolitan',4,'1997-06-15',21);


insert into performance values (1,1,1,21,1);
insert into performance values (2,1,3,21,1);
insert into performance values (3,1,5,21,1);
insert into performance values (4,1,2,1,2);
insert into performance values (5,2,4,21,2);
insert into performance values (6,2,6,21,2);
insert into performance values (7,4,19,9,3);
insert into performance values (8,4,20,10,3);
insert into performance values (9,5,12,10,4);
insert into performance values (10,5,13,11,4);
insert into performance values (11,3,5,13,5);
insert into performance values (12,3,6,13,5);
insert into performance values (13,3,7,13,5);
insert into performance values (14,6,20,14,6);
insert into performance values (15,8,12,15,7);
insert into performance values (16,9,16,21,8);
insert into performance values (17,9,17,21,8);
insert into performance values (18,9,18,21,8);
insert into performance values (19,9,19,21,8);
insert into performance values (20,4,12,10,3);

