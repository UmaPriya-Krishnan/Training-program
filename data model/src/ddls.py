import sys
from datetime import datetime
sys.path.append(r"C:\Users\mohan\Desktop\py_sql\src")
import connection
import logfile

class dbconn:
    def __init__(self):
        """Connection with the database is established and the functions for table creation are invoked"""
        try:
            mydb = connection.con()
            mycursor = mydb.cursor()
            self.createSTUDENT_REFERENCE(mydb, mycursor)
            self.createFpayment(mydb, mycursor)
            self.createFacademics(mydb, mycursor)
            self.createFstudent(mydb, mycursor)
            self.createFattendence(mydb, mycursor)
            self.createFplacement(mydb, mycursor)

            self.PaymentDetails(mydb, mycursor)
            self.Degree(mydb, mycursor)
            self.ExamDetails(mydb, mycursor)
            self.GradeDetails(mydb, mycursor)
            self.CourseDetails(mydb, mycursor)
            self.DepartmentDetails(mydb, mycursor)
            self.StaffDetails(mydb, mycursor)
            self.CalenderDetails(mydb, mycursor)
            self.PlacementDetails(mydb, mycursor)
            
            
            self.InsertPaymentDetails(mydb, mycursor)
            self.InserDegree(mydb, mycursor)
            self.InsertExamDetails(mydb, mycursor)
            self.InsertGradeDetails(mydb, mycursor)
            self.InsertCourseDetails(mydb, mycursor)
            self.InsertDeptDetails(mydb, mycursor)
            self.InsertStaffDetails(mydb, mycursor)
            self.InsertCalendarDetails(mydb, mycursor)
            self.InsertPlacementDetails(mydb, mycursor)
            
        except Exception as e:
            print("Error:",e)

    def createSTUDENT_REFERENCE(self, mydb, mycursor):
        """Creation of student reference table which contains details of the student."""
        try:
            sql='''create table if not exists STUDENT_REFERENCE(STUDENT_ID BIGINT PRIMARY KEY NOT NULL,
                     NAME     VARCHAR(45)   NOT NULL,
                     DOB       DATE       NOT NULL,
                     GENDER    VARCHAR(10),
                     GUARDIAN_NAME  VARCHAR(45),
                     ADDRESS    VARCHAR(50),
                     PHONE_NO   BIGINT,
                     DOJ    DATE,
                     STUDENT_START_DATE DATETIME,
                     STUDENT_END_DATE   DATETIME)'''
            #mycursor.execute("drop table student_reference")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("STUDENT_REFERENCE created!")
        except Exception as e:
            print("Error:", e)

    def createFpayment(self, mydb, mycursor):
        """Creation of fact table for payment."""
        try:
            sql='''create table if not exists FactPayment(STUDENT_ID BIGINT NOT NULL,
                     FEE_ID    VARCHAR(10)   NOT NULL,
                     PAYMENT_ID VARCHAR(9),
                     PAYMENT_FACT_START_DATE DATETIME,
                     PAYMENT_FACT_END_DATE   DATETIME)'''
            #mycursor.execute("drop table FactPayment")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("Fact : Payment created!")
        except Exception as e:
            print("Error:", e)

    def createFacademics(self, mydb, mycursor):
        """Creation of fact table for academics."""
        try:
            sql='''create table if not exists FactAcademics(STUDENT_ID BIGINT NOT NULL,
                     DEGREE_ID  BIGINT,
                     EXAM_ID    INT,
                     MARKS  INT,
                     COURSE_ID  VARCHAR(9),
                     GRADE_ID   CHAR(2),
                     ACADEMICS_START_DATE DATETIME,
                     ACADEMICS_END_DATE   DATETIME)'''
            #mycursor.execute("drop table FactAcademics")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("Fact : Academics created!")
        except Exception as e:
            print("Error:", e)

    def createFstudent(self, mydb, mycursor):
        """Creation of fact table for student."""
        try:
            sql='''create table if not exists FactStudent(STUDENT_ID BIGINT NOT NULL,
                     DEP_ID    VARCHAR(9)   NOT NULL,
                     COURSE_ID VARCHAR(9),
                     STAFF_ID   VARCHAR(9),
                     STUDENT_FACT_START_DATE DATETIME,
                     STUDENT_FACT_END_DATE   DATETIME)'''
            #mycursor.execute("drop table FactStudent")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("Fact : Student created!")
        except Exception as e:
            print("Error:", e)

    def createFattendence(self, mydb, mycursor):
        """Creation of fact table for attendance."""
        try:
            sql='''create table if not exists FactAttendence(STUDENT_ID BIGINT NOT NULL,
                     TIME_ID    INT,
                     CURDATE       DATE,
                     COURSE_ID  VARCHAR(9),
                     STAFF_ID   VARCHAR(9),
                     ATTENDENCE VARCHAR(2),
                     ATTENDENCE_START_DATE DATETIME,
                     ATTENDENCE_END_DATE   DATETIME)'''
            #mycursor.execute("drop table FactAttendence")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("FACT : Attendence created!")
        except Exception as e:
            print("Error:", e)

    def createFplacement(self, mydb, mycursor):
        """Creation of fact table for placement."""
        try:
            sql='''create table if not exists FactPlacement(STUDENT_ID BIGINT NOT NULL,
                     DEP_ID    VARCHAR(9),
                     COMPANY_ID VARCHAR(9),
                     HIRED  VARCHAR(5),
                     PLACEMENT_FACT_START_DATE DATETIME,
                     PLACEMENT_FACT_END_DATE   DATETIME)'''
            #mycursor.execute("drop table FactPlacement")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("Fact : Placement created!")
        except Exception as e:
            print("Error:", e)

    def PaymentDetails(self, mydb, mycursor):
        """Creation of dimension table for payment details."""
        try:
            sql = '''create table if not exists payment_details(FEE_ID VARCHAR(10) NOT NULL PRIMARY KEY,
                        FEES   BIGINT,
                        FEES_TYPE  VARCHAR(15),
                        PAYMENT_START_DATE DATETIME,
                        PAYMENT_END_DATE   DATETIME)'''
            #mycursor.execute("drop table payment_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Payment_Details created!")
        except Exception as e:
            print("Error:", e)

    def Degree(self, mydb, mycursor):
        """Creation of dimension table for degree."""
        try:
            sql = '''create table if not exists degree(DEGREE_ID BIGINT NOT NULL PRIMARY KEY,
                        DEGREE_TYPE   VARCHAR(5),
                        DURATION   INT,
                        DEGREE_START_DATE DATETIME,
                        DEGREE_END_DATE   DATETIME)'''
            #mycursor.execute("drop table degree")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Details created!")
        except Exception as e:
            print("Error:", e)

    def ExamDetails(self, mydb, mycursor):
        """Creation of dimension table for exam details."""
        try:
            sql = '''create table if not exists exam_details(EXAM_ID INT NOT NULL PRIMARY KEY,
                        EXAM_TYPE   VARCHAR(3),
                        EXAM_DESCRIPTION    VARCHAR(15),
                        EXAM_START_DATE DATETIME,
                        EXAM_END_DATE   DATETIME)'''
            #mycursor.execute("drop table exam_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Exam_Details created!")
        except Exception as e:
            print("Error:", e)

    def GradeDetails(self, mydb, mycursor):
        """Creation of dimension table for grade details."""
        try:
            sql = '''create table if not exists grade_details(GRADE_ID CHAR(2) NOT NULL PRIMARY KEY,
                        GRADE_DESCRIPTION    CHAR(20),
                        GRADE_START_DATE DATETIME,
                        GRADE_END_DATE   DATETIME)'''
            #mycursor.execute("drop table grade_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Grade_Details created!")
        except Exception as e:
            print("Error:", e)

    def CourseDetails(self, mydb, mycursor):
        """Creation of dimension table for course details."""
        try:
            sql = '''create table if not exists course_details(COURSE_ID VARCHAR(9) NOT NULL PRIMARY KEY,
                        COURSE_NAME VARCHAR(20),
                        COURSE_START_DATE DATETIME,
                        COURSE_END_DATE   DATETIME)'''
            #mycursor.execute("drop table course_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Course_Details created!")
        except Exception as e:
            print("Error:", e)

    def DepartmentDetails(self, mydb, mycursor):
        """Creation of dimension table for  department details."""
        try:
            sql = '''create table if not exists department_details(DEP_ID VARCHAR(9) NOT NULL PRIMARY KEY,
                        DEP_NAME VARCHAR(40),
                        DEP_START_DATE DATETIME,
                        DEP_END_DATE   DATETIME)'''
            #mycursor.execute("drop table department_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Dep_Details created!")
        except Exception as e:
            print("Error:", e)

    def StaffDetails(self, mydb, mycursor):
        """Creation of dimension table for  staff details."""
        try:
            sql = '''create table if not exists staff_details(STAFF_ID VARCHAR(9) NOT NULL PRIMARY KEY,
                        STAFF_NAME VARCHAR(25),
                        STAFF_DOJ   DATE,
                        STAFF_START_DATE DATETIME,
                        STAFF_END_DATE   DATETIME)'''
            #mycursor.execute("drop table staff_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Staff_Details created!")
        except Exception as e:
            print("Error:", e)

    def CalenderDetails(self, mydb, mycursor):
        """Creation of dimension table for  calender details."""
        try:
            sql = '''create table if not exists calender_details(TIME_ID INT NOT NULL PRIMARY KEY,
                        HOLIDAY DATE,
                        HOLIDAY_START_DATE DATETIME,
                        HOLIDAY_END_DATE   DATETIME)'''
            #mycursor.execute("drop table calender_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Calender_Details created!")
        except Exception as e:
            print("Error:", e)

    def PlacementDetails(self, mydb, mycursor):
        """Creation of dimension table for  placement details."""
        try:
            sql = '''create table if not exists placement_details(COMPANY_ID VARCHAR(9) NOT NULL PRIMARY KEY,
                        COMPANY_NAME    VARCHAR(15),
                        PLACEMENT_VENUE VARCHAR(50),
                        PLACEMENT_DATE  DATE,
                        PLACEMENT_START_DATE DATETIME,
                        PLACEMENT_END_DATE   DATETIME)'''
            #mycursor.execute("drop table placement_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Placement_Details created!")
        except Exception as e:
            print("Error:", e)
    def InsertPaymentDetails(self,mydb,mycursor):
        try:        
            filename = 'C:\\Users\\mohan\\Desktop\\csv\\dimension\\payment_dim.csv'
            with open(filename,'r') as fr:
                for line in fr.readlines():
                    col_value = line.replace('\n','').split(',')
                    insert_query = ("insert into payment_details(FEE_ID, FEES, FEES_TYPE, PAYMENT_START_DATE, PAYMENT_END_DATE) values('{}','{}','{}','{}','{}')" 
                                       .format(col_value[0],col_value[1],col_value[2],datetime.now(),col_value[3]))
                  
                    mycursor.execute(insert_query)
            mydb.commit()
            l = logfile.logger()
            l.info("Values inserted into the payment_details table successfully!")
        except Exception as e:
            print("Error:",e)

    def InserDegree(self,mydb,mycursor):
        try:        
            filename = 'C:\\Users\\mohan\\Desktop\\csv\\dimension\\degree_dim.csv'
            with open(filename,'r') as fr:
                for line in fr.readlines():
                    col_value = line.replace('\n','').split(',')
                    insert_query = ("insert into degree(DEGREE_ID, DEGREE_TYPE, DURATION,DEGREE_START_DATE,DEGREE_END_DATE) values('{}','{}','{}', '{}','{}')"
                                    .format(col_value[0], col_value[1], col_value[2], datetime.now(), col_value[3])) 
                  
                    mycursor.execute(insert_query)
            mydb.commit()
            l = logfile.logger()
            l.info("Values inserted into the degree table successfully!")
        except Exception as e:
            print("Error:",e)


    def InsertExamDetails(self,mydb,mycursor):
        try:        
            filename = 'C:\\Users\\mohan\\Desktop\\csv\\dimension\\exams_dim.csv'
            with open(filename,'r') as fr:
                for line in fr.readlines():
                    col_value = line.replace('\n','').split(',')
                    insert_query =("insert into exam_details(EXAM_ID, EXAM_TYPE, EXAM_DESCRIPTION, EXAM_START_DATE,EXAM_END_DATE)values('{}','{}','{}','{}','{}')"
                                    .format(col_value[0],col_value[1],col_value[2],datetime.now(),col_value[3]))
                  
                    mycursor.execute(insert_query)
            mydb.commit()
            l = logfile.logger()
            l.info("Values inserted into the exam_details table successfully!")
        except Exception as e:
            print("Error:",e)

    def InsertGradeDetails(self,mydb,mycursor):
        try:        
            filename = 'C:\\Users\\mohan\\Desktop\\csv\\dimension\\grade_dim.csv'
            with open(filename,'r') as fr:
                for line in fr.readlines():
                    col_value = line.replace('\n','').split(',')
                    insert_query = ("insert into grade_details(GRADE_ID, GRADE_DESCRIPTION, GRADE_START_DATE, GRADE_END_DATE) values('{}','{}','{}','{}')"
                                    .format(col_value[0],col_value[1],datetime.now(),col_value[2]))
                  
                    mycursor.execute(insert_query)
            mydb.commit()
            l = logfile.logger()
            l.info("Values inserted into the grade_details table successfully!")
        except Exception as e:
            print("Error:",e)

    def InsertCourseDetails(self,mydb,mycursor):
        try:        
            filename = 'C:\\Users\\mohan\\Desktop\\csv\\dimension\\course_dim.csv'
            with open(filename,'r') as fr:
                for line in fr.readlines():
                    col_value = line.replace('\n','').split(',')
                    insert_query = ("insert into course_details(COURSE_ID, COURSE_NAME, COURSE_START_DATE, COURSE_END_DATE) values('{}','{}','{}','{}')"
                                    .format(col_value[0],col_value[1],datetime.now(),col_value[2]))
                  
                    mycursor.execute(insert_query)
            mydb.commit()
            l = logfile.logger()
            l.info("Values inserted into the course_details table successfully!")
        except Exception as e:
            print("Error:",e)

    def InsertDeptDetails(self,mydb,mycursor):
        try:        
            filename = 'C:\\Users\\mohan\\Desktop\\csv\\dimension\\department_dim.csv'
            with open(filename,'r') as fr:
                for line in fr.readlines():
                    col_value = line.replace('\n','').split(',')
                    insert_query = ("insert into department_details(DEP_ID, DEP_NAME, DEP_START_DATE, DEP_END_DATE) values('{}','{}','{}','{}')"
                                    .format(col_value[0],col_value[1],col_value[2], datetime.now(),col_value[2]))
 
                  
                    mycursor.execute(insert_query)
            mydb.commit()
            l = logfile.logger()
            l.info("Values inserted into the department_details table successfully!")
        except Exception as e:
            print("Error deo:",e)

    def InsertStaffDetails(self,mydb,mycursor):
        try:        
            filename = 'C:\\Users\\mohan\\Desktop\\csv\\dimension\\staff_dim.csv'
            with open(filename,'r') as fr:
                for line in fr.readlines():
                    col_value = line.replace('\n','').split(',')
                    insert_query = ("insert into staff_details(STAFF_ID, STAFF_NAME, STAFF_DOJ, STAFF_START_DATE, STAFF_END_DATE) values('{}','{}','{}','{}','{}')"
                                    .format(col_value[0],col_value[1],col_value[2], datetime.now(),col_value[3]))
                    mycursor.execute(insert_query)
            mydb.commit()
            l = logfile.logger()
            l.info("Values inserted into the Staff_details table successfully!")
        except Exception as e:
            print("Error:",e)

    def InsertPlacementDetails(self,mydb,mycursor):
        try:        
            filename = 'C:\\Users\\mohan\\Desktop\\csv\\dimension\\company_dim.csv'
            with open(filename,'r') as fr:
                for line in fr.readlines():
                    col_value = line.replace('\n','').split(',')
                    insert_query = ("insert into placement_details(COMPANY_ID, COMPANY_NAME, PLACEMENT_VENUE, PLACEMENT_DATE, PLACEMENT_START_DATE, PLACEMENT_END_DATE) values('{}','{}','{}','{}','{}','{}')"
								.format(col_value[0],col_value[1], col_value[2], col_value[3], datetime.now(), col_value[4]))
                    mycursor.execute(insert_query)
            mydb.commit()
            l = logfile.logger()
            l.info("Values inserted into the placement_details table successfully!")
        except Exception as e:
            print("Error:",e)

    def InsertCalendarDetails(self,mydb,mycursor):
        try:        
            filename = 'C:\\Users\\mohan\\Desktop\\csv\\dimension\\time_dim.csv'
            with open(filename,'r') as fr:
                for line in fr.readlines():
                    col_value = line.replace('\n','').split(',')
                    insert_query = ("insert into calender_details(TIME_ID, HOLIDAY, HOLIDAY_START_DATE, HOLIDAY_END_DATE) values('{}','{}','{}','{}')" 
                                    .format(col_value[0],col_value[1], datetime.now(), col_value[2]))
                  
                    mycursor.execute(insert_query)
            mydb.commit()
            l = logfile.logger()
            l.info("Values inserted into the calendar_details table successfully!")
        except Exception as e:
            print("Error:",e)

obj=dbconn()



