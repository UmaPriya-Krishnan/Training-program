create table if not exists dimension_staff_details(STAFF_ID VARCHAR(9) NOT NULL PRIMARY KEY,
                        STAFF_NAME VARCHAR(25),
                        STAFF_DOJ   DATE,
                        STAFF_START_DATE DATETIME,
                        STAFF_END_DATE   DATETIME);