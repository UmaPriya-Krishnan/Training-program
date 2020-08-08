create table if not exists dimension_calender_details(TIME_ID VARCHAR(5) PRIMARY KEY,
                        HOLIDAY DATE,
                        HOLIDAY_START_DATE DATETIME,
                        HOLIDAY_END_DATE  DATETIME);