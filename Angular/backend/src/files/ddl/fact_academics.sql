create table if not exists fact_academics(STUDENT_ID BIGINT NOT NULL,
                     DEGREE_ID  BIGINT,
                     EXAM_ID    INT,
                     MARKS  INT,
                     COURSE_ID  VARCHAR(9),
                     GRADE_ID   CHAR(2),
                     ACTIVE_FLAG CHAR(1),
                     ACADEMICS_START_DATE DATETIME,
                     ACADEMICS_END_DATE   DATETIME,
					 FOREIGN KEY (STUDENT_ID) REFERENCES details_main (STUDENT_ID),
					 FOREIGN KEY(DEGREE_ID) REFERENCES dimension_degree_details(DEGREE_ID),
					 FOREIGN KEY(COURSE_ID) REFERENCES dimension_course_details(COURSE_ID),
					 FOREIGN KEY(EXAM_ID) REFERENCES dimension_exam_details(EXAM_ID),
					 FOREIGN KEY(GRADE_ID) REFERENCES dimension_grade_details(GRADE_ID));