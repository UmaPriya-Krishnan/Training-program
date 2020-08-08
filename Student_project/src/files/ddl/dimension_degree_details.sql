create table if not exists dimension_degree_details(DEGREE_ID BIGINT NOT NULL PRIMARY KEY,
                        DEGREE_TYPE   VARCHAR(5),
                        DURATION   INT,
                        DEGREE_START_DATE DATETIME,
                        DEGREE_END_DATE   DATETIME);