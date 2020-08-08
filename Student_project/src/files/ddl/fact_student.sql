create table if not exists fact_student(STUDENT_ID BIGINT NOT NULL,
                     DEP_ID    VARCHAR(9)   NOT NULL,
                     COURSE_ID VARCHAR(9),
                     STAFF_ID   VARCHAR(9),
                     STUDENT_FACT_START_DATE DATETIME,
                     STUDENT_FACT_END_DATE   DATETIME,
					 FOREIGN KEY(DEP_ID) REFERENCES dimension_department_details(DEP_ID),
					 FOREIGN KEY(COURSE_ID) REFERENCES dimension_course_details(COURSE_ID),
					 FOREIGN KEY (STUDENT_ID) REFERENCES details_main(STUDENT_ID));