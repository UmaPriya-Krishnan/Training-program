create table if not exists fact_placement(STUDENT_ID BIGINT NOT NULL,
                     DEP_ID    VARCHAR(9),
                     COMPANY_ID VARCHAR(9),
                     HIRED  VARCHAR(5),
                     PLACEMENT_FACT_START_DATE DATETIME,
                     PLACEMENT_FACT_END_DATE   DATETIME,
					 FOREIGN KEY(STUDENT_ID) REFERENCES details_main (STUDENT_ID),
					 FOREIGN KEY(DEP_ID) REFERENCES dimension_department_details(DEP_ID),
					 FOREIGN KEY(COMPANY_ID) REFERENCES dimension_placement_details(COMPANY_ID));